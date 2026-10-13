import { duplicates, type Issue, issue } from "../core/diagnostics.helper";
import type {
  CapabilityProfileV2,
  MainObjective,
} from "../schemas/scenario-capability.schema";
import { isSameOrRequiredPredecessor } from "./objective-ancestry.helper";
import { paymentReceiptMatches } from "./payment-receipt.helper";
import { validateRequirementCausality } from "./requirement-causality.validator";

const resourceNames = ["food", "wood", "gold", "stone"] as const;
export function validateScenarioCapability(
  profile: CapabilityProfileV2,
): Issue[] {
  const districtIds = profile.districts;
  const out: Issue[] = [];
  const add = (code: string, id: string, message: string) =>
    out.push(issue(code, id, message));
  const entities = new Map(
    profile.worldContract.entities.map((e) => [e.id, e]),
  );
  const zones = new Map(profile.worldContract.zones.map((z) => [z.id, z]));
  const objectives = new Map(profile.objectivePlan.map((o) => [o.id, o]));
  const objectiveIds = profile.objectivePlan.map((o) => o.id);
  const sideIds = new Set(profile.secondaryObjectives.map((o) => o.id));
  const phaseIds = new Set(profile.stateMachine.states);
  const reqOwners = new Map<string, string>();
  const receiptOwners = new Map<string, string>();
  const allWorldIds = [
    ...profile.worldContract.entities.map((e) => e.id),
    ...profile.worldContract.zones.map((z) => z.id),
    ...profile.secondaryObjectives.flatMap((o) =>
      o.world.entities.map((e) => e.id),
    ),
    ...profile.secondaryObjectives.flatMap((o) =>
      o.world.zones.map((z) => z.id),
    ),
  ];

  for (const id of duplicates(allWorldIds))
    add("capability.world-id", id, "ID de entidad/zona repetido en el perfil");
  for (const id of duplicates(objectiveIds))
    add("capability.objective-id", id, "Objetivo compuesto repetido");
  for (const id of duplicates(profile.secondaryObjectives.map((o) => o.id)))
    add("capability.secondary-id", id, "Objetivo secundario repetido");
  if (
    profile.secondaryObjectives.length < 6 ||
    profile.secondaryObjectives.length > 8
  )
    add(
      "capability.secondary-count",
      profile.profile,
      "El perfil requiere entre seis y ocho objetivos secundarios",
    );
  if (
    new Set(districtIds).size !== districtIds.length ||
    districtIds.length === 0
  )
    add(
      "capability.districts",
      profile.profile,
      "Los distritos deben estar declarados y ser únicos",
    );

  for (const entity of entities.values()) {
    if (!districtIds.includes(entity.initialHub))
      add("capability.entity-hub", entity.id, "Origen de entidad no declarado");
  }
  for (const zone of zones.values()) {
    if (!districtIds.includes(zone.hub))
      add("capability.zone-hub", zone.id, "Distrito de zona no declarado");
  }
  for (const group of profile.worldContract.survivorGroups) {
    if (new Set(group.entities).size !== group.entities.length)
      add(
        "capability.survivor-identity",
        profile.profile,
        "Un superviviente no puede contar por varios IDs repetidos",
      );
    if (group.minimumAliveOrAlreadySafe > new Set(group.entities).size)
      add(
        "capability.survivor-threshold",
        group.entities[0] ?? profile.profile,
        "Umbral de supervivientes imposible",
      );
    for (const id of group.entities)
      if (!entities.has(id))
        add("capability.survivor-entity", id, "Superviviente no declarado");
  }

  for (const objective of profile.objectivePlan) {
    const context = objective.id;
    if (!districtIds.includes(objective.targetHub))
      add(
        "capability.objective-hub",
        context,
        "Distrito objetivo no declarado",
      );
    if (!phaseIds.has(objective.phase))
      add(
        "capability.objective-phase",
        context,
        "Fase del objetivo no declarada",
      );
    if (
      objective.threshold !== objective.countLedger.required ||
      objective.predicate.requiredCount !== objective.threshold
    )
      add(
        "capability.objective-threshold",
        context,
        "Los umbrales declarados divergen",
      );
    for (const dep of objective.after)
      if (!objectives.has(dep))
        add(
          "capability.objective-dependency",
          context,
          `Objetivo previo inexistente: ${dep}`,
        );
    for (const dep of objective.after)
      if (sideIds.has(dep))
        add(
          "capability.secondary-dependency",
          context,
          "Los secundarios no pueden bloquear objetivos principales",
        );
    const predicate = objective.predicate;
    const reqIds = predicate.requirements.map((r) => r.id);
    for (const duplicate of duplicates(reqIds))
      add(
        "capability.requirement-id",
        `${context}.${duplicate}`,
        "Predicado repetido",
      );
    if (
      new Set(reqIds).size !== reqIds.length ||
      reqIds.some((id) => !predicate.requiredLedgers.includes(id)) ||
      predicate.requiredLedgers.some((id) => !reqIds.includes(id))
    )
      add(
        "capability.and-ledgers",
        context,
        "Todos los requisitos deben corresponder exactamente a ledgers requeridos",
      );
    if (predicate.operator !== "all" || !predicate.allRequired)
      add(
        "capability.and",
        context,
        "La composición solo permite AND estricto",
      );

    for (const entity of objective.entities) {
      if (!entities.has(entity.id))
        add(
          "capability.objective-entity",
          entity.id,
          "Entidad de objetivo no está en worldContract",
        );
      if (!districtIds.includes(entity.initialHub))
        add(
          "capability.entity-hub",
          entity.id,
          "Origen de entidad no declarado",
        );
    }
    for (const req of predicate.requirements) {
      const reqContext = `${context}.${req.id}`;
      // Every identity list is a set, including lists whose counts are checked elsewhere.
      for (const [field, ids] of Object.entries(req)) {
        if (
          [
            "entities",
            "zones",
            "waves",
            "inputEntities",
            "outputEntities",
            "departingEntities",
            "receivingZones",
            "inputRecords",
            "carriedRecords",
            "blockingEnemies",
          ].includes(field) &&
          Array.isArray(ids) &&
          new Set(ids).size !== ids.length
        )
          add(
            "capability.identity-list",
            reqContext,
            `Identidades repetidas en ${field}`,
          );
      }
      const requirementKey = `${context}.${req.id}`;
      if (reqOwners.has(requirementKey))
        add(
          "capability.requirement-id",
          requirementKey,
          "Predicado repetido en el objetivo",
        );
      reqOwners.set(requirementKey, context);
      const entityRefs: string[] = [];
      const zoneRefs: string[] = [];
      switch (req.kind) {
        case "entity-state":
          if (req.arrivalAfterDeparture) {
            const ref = req.arrivalAfterDeparture;
            const departure = objectives
              .get(ref.objective)
              ?.predicate.requirements.find((r) => r.id === ref.requirement);
            if (
              req.state !== "arrived" ||
              !req.destinations ||
              departure?.kind !== "ordered-departure" ||
              !req.entities.every((id) =>
                departure.departingEntities.includes(id),
              ) ||
              !isSameOrRequiredPredecessor(profile, ref.objective, objective.id)
            )
              add(
                "capability.arrival-departure",
                reqContext,
                "La llegada debe referenciar una salida de las mismas identidades en este objetivo o en un predecesor obligatorio",
              );
          }
          if (new Set(req.entities).size !== req.entities.length)
            add(
              "capability.entity-identity-duplicate",
              reqContext,
              "Cada identidad se cuenta una sola vez en un predicado",
            );
          entityRefs.push(...req.entities);
          entityRefs.push(
            ...(req.inputRecords ?? []),
            ...(req.carriedRecords ?? []),
          );
          if (req.carriedRecords?.length)
            add(
              "capability.inventory-contract",
              reqContext,
              "El transporte de inventario requiere contrato de propiedad tipado; no se certifica por texto libre",
            );
          if (req.destinations) {
            if (
              Object.keys(req.destinations).length !== req.entities.length ||
              req.entities.some((id) => !req.destinations?.[id])
            )
              add(
                "capability.entity-destination",
                reqContext,
                "Cada entidad debe tener un destino individual",
              );
            for (const [entityId, zoneId] of Object.entries(req.destinations)) {
              zoneRefs.push(zoneId);
              const entity = entities.get(entityId);
              const zone = zones.get(zoneId);
              if (
                entity &&
                zone &&
                entity.initialHub === zone.hub &&
                Math.hypot(
                  entity.offsetTiles[0] - zone.offsetTiles[0],
                  entity.offsetTiles[1] - zone.offsetTiles[1],
                ) <= zone.radiusTiles
              )
                add(
                  "capability.initial-arrival",
                  entityId,
                  "Una entidad no puede contar por aparecer dentro de su destino",
                );
            }
          }
          if (
            req.distinctDestinationCount !== undefined ||
            req.minimumPerDestination !== undefined
          ) {
            const counts = new Map<string, number>();
            for (const entityId of req.entities) {
              const zoneId = req.destinations?.[entityId];
              if (zoneId) counts.set(zoneId, (counts.get(zoneId) ?? 0) + 1);
            }
            if (
              req.state !== "arrived" ||
              !req.destinations ||
              counts.size < (req.distinctDestinationCount ?? 0) ||
              (req.minimumPerDestination !== undefined &&
                [...counts.values()].some(
                  (count) => count < (req.minimumPerDestination ?? 0),
                ))
            )
              add(
                "capability.destination-distribution",
                reqContext,
                "Los mínimos por destino requieren llegadas tipadas y suficientes identidades asignadas a cada zona",
              );
          }
          if (req.eligibleEntitiesFromLedger) {
            const source = objectives.get(
              req.eligibleEntitiesFromLedger.objective,
            );
            const eligibility = req.eligibleEntitiesFromLedger;
            const exported = source?.predicate.exportedLedgers?.find(
              (l) =>
                l.id === eligibility.ledger && l.operator === "intersection",
            );
            const sourceRequirements =
              exported?.fromRequirements.map((id) =>
                source?.predicate.requirements.find(
                  (candidate) => candidate.id === id,
                ),
              ) ?? [];
            const arrivalSets = sourceRequirements.map((candidate) =>
              candidate?.kind === "paired-delivery"
                ? new Set(candidate.pairs.map((pair) => pair.receiver))
                : candidate?.kind === "entity-state" &&
                    candidate.state === "arrived"
                  ? new Set(candidate.entities)
                  : new Set<string>(),
            );
            const commonEligibleIds = [...(arrivalSets[0] ?? [])].filter((id) =>
              arrivalSets.every((set) => set.has(id)),
            );
            if (
              !exported ||
              exported.minimumCount < req.requiredCount ||
              sourceRequirements.some(
                (candidate) =>
                  !candidate ||
                  !(
                    candidate.kind === "paired-delivery" ||
                    (candidate.kind === "entity-state" &&
                      candidate.state === "arrived")
                  ),
              ) ||
              commonEligibleIds.length < req.requiredCount ||
              req.entities.some((id) => !commonEligibleIds.includes(id))
            )
              add(
                "capability.survivor-intersection",
                reqContext,
                "La retirada debe usar una intersección tipada por IDs comunes realmente recibidos",
              );
          }
          if (req.generatedByReceipts)
            for (const receipt of req.generatedByReceipts) {
              const producer = objectives
                .get(receipt.fromObjective)
                ?.predicate.requirements.find(
                  (r) => r.id === receipt.fromRequirement,
                );
              if (
                !producer ||
                producer.kind !== "entity-state" ||
                producer.destinations?.[receipt.receivedEntity] !==
                  receipt.destination ||
                !req.entities.includes(receipt.output)
              )
                add(
                  "capability.receipt-entity",
                  reqContext,
                  "La copia debe proceder de un recibo real de entrega",
                );
            }
          break;
        case "area-state":
        case "civilian-protection":
        case "forbidden-entry":
        case "hold-area":
          zoneRefs.push(...req.zones);
          if (
            req.kind === "civilian-protection" &&
            (!phaseIds.has(req.activeFrom) ||
              !phaseIds.has(req.activeUntil) ||
              req.activeFrom === req.activeUntil)
          )
            add(
              "capability.protection-interval",
              reqContext,
              "La protección civil requiere fases de inicio y fin distintas y existentes",
            );
          if ("blockingEnemies" in req)
            entityRefs.push(...(req.blockingEnemies ?? []));
          if (
            req.kind === "forbidden-entry" &&
            req.actorSelector !== "all-player-controlled-units"
          )
            add(
              "capability.forbidden-entry",
              reqContext,
              "La prohibición debe cubrir todas las unidades controladas por el jugador",
            );
          break;
        case "resource-transaction": {
          zoneRefs.push(...req.receivingZones);
          if (req.account !== "spendable" || !req.atomic || !req.once)
            add(
              "capability.transaction",
              reqContext,
              "Los pagos deben ser únicos y atómicos en spendable",
            );
          if (receiptOwners.has(req.paidFlag))
            add(
              "capability.receipt",
              req.paidFlag,
              "Recibo de pago reutilizado",
            );
          receiptOwners.set(req.paidFlag, context);
          if (
            resourceNames.every(
              (resource) => (req.amounts[resource] ?? 0) === 0,
            ) ||
            req.receivingZones.length < 1
          )
            add(
              "capability.transaction-empty",
              reqContext,
              "La transacción requiere importe positivo y al menos un receptor declarado",
            );
          if (new Set(req.receivingZones).size !== req.receivingZones.length)
            add(
              "capability.transaction-receivers",
              reqContext,
              "Los receptores de distribución deben ser distintos",
            );
          for (let i = 0; i < req.receivingZones.length; i++) {
            for (const otherId of req.receivingZones.slice(i + 1)) {
              const left = zones.get(req.receivingZones[i] ?? "");
              const right = zones.get(otherId);
              if (
                left &&
                right &&
                left.hub === right.hub &&
                Math.hypot(
                  left.offsetTiles[0] - right.offsetTiles[0],
                  left.offsetTiles[1] - right.offsetTiles[1],
                ) <=
                  left.radiusTiles + right.radiusTiles
              )
                add(
                  "capability.transaction-overlap",
                  reqContext,
                  "Los distritos receptores no están separados",
                );
            }
          }
          const allocationIds = Object.keys(req.allocations);
          if (
            allocationIds.length !== req.receivingZones.length ||
            req.receivingZones.some((id) => !req.allocations[id]) ||
            allocationIds.some((id) => !req.receivingZones.includes(id))
          )
            add(
              "capability.transaction-allocation",
              reqContext,
              "Asignaciones y receptores deben coincidir exactamente",
            );
          for (const resource of resourceNames) {
            const total = req.amounts[resource] ?? 0;
            const allocated = Object.values(req.allocations).reduce(
              (sum, amount) => sum + (amount[resource] ?? 0),
              0,
            );
            if (allocated !== total)
              add(
                "capability.transaction-balance",
                reqContext,
                `Asignación ${resource} no conserva el total`,
              );
          }
          break;
        }
        case "minimum-stock":
          if (
            req.atHub !== undefined ||
            req.accountEntityIds !== undefined ||
            req.maximumNavigableDistanceTiles !== undefined
          )
            add(
              "capability.stock-location-contract",
              reqContext,
              "El stock físico requiere inventario por portador y distancias navegables tipadas; no se acredita con saldo global",
            );
          entityRefs.push(...(req.accountEntityIds ?? []));
          if (req.atHub) {
            // Hubs are checked below against the declared district table.
            if (!districtIds.includes(req.atHub))
              add(
                "capability.minimum-stock-hub",
                reqContext,
                "Stock asociado a distrito inexistente",
              );
          }
          break;
        case "paired-delivery": {
          entityRefs.push(
            ...req.pairs.flatMap((pair) => [pair.cargo, pair.receiver]),
          );
          zoneRefs.push(req.destination);
          if (
            new Set(req.pairs.map((pair) => pair.cargo)).size !==
              req.pairs.length ||
            new Set(req.pairs.map((pair) => pair.receiver)).size !==
              req.pairs.length
          )
            add(
              "capability.paired-identity",
              reqContext,
              "Carga y receptor deben formar parejas de IDs únicos",
            );
          const familyGroup = profile.worldContract.survivorGroups.find(
            (group) =>
              req.pairs.every((pair) => group.entities.includes(pair.receiver)),
          );
          if (
            !familyGroup ||
            req.requiredCount < familyGroup.minimumAliveOrAlreadySafe ||
            req.requiredCount > req.pairs.length
          )
            add(
              "capability.paired-survivors",
              reqContext,
              "Las parejas deben usar las mismas familias supervivientes y el umbral protegido",
            );
          break;
        }
        case "route-choice":
          break;
        case "finite-wave-resolution":
          if (
            req.requiredCount > new Set(req.waves).size ||
            req.waves.some(
              (id) =>
                !profile.enemyRoster.mobilizations.some(
                  (wave) => wave.id === id,
                ),
            )
          )
            add(
              "capability.wave-resolution",
              reqContext,
              "El umbral requiere oleadas distintas y declaradas",
            );
          break;
        case "receipt-exists":
          if (!paymentReceiptMatches(profile, req))
            add(
              "capability.receipt-source",
              reqContext,
              "El recibo requiere productor único, objetivo de origen e importe exacto",
            );
          if (req.newDebit)
            add(
              "capability.receipt-debit",
              reqContext,
              "Consultar un recibo no puede volver a debitar recursos",
            );
          break;
        case "derived-token":
          entityRefs.push(...req.inputEntities, ...req.outputEntities);
          if (new Set(req.outputEntities).size !== req.outputEntities.length)
            add(
              "capability.derived-token",
              reqContext,
              "Cada salida derivada necesita un ID único y persistente",
            );
          for (const receipt of req.requiredPaymentReceipts ?? []) {
            if (!paymentReceiptMatches(profile, receipt))
              add(
                "capability.derived-payment",
                reqContext,
                "La fabricación exige un recibo con productor único e importe exacto",
              );
            if (
              !isSameOrRequiredPredecessor(
                profile,
                receipt.fromObjective,
                objective.id,
              )
            )
              add(
                "capability.derived-payment-order",
                reqContext,
                "El pago de fabricación debe pertenecer al mismo objetivo o a un predecesor obligatorio",
              );
          }
          break;
        case "ordered-departure":
          entityRefs.push(...req.departingEntities);
          if (!objectives.has(req.receiptObjective))
            add(
              "capability.departure-receipt",
              reqContext,
              "Salida ordenada depende de un objetivo inexistente",
            );
          if (req.receiptRequirement) {
            const receipt = objectives
              .get(req.receiptObjective)
              ?.predicate.requirements.find(
                (item) => item.id === req.receiptRequirement,
              );
            if (!receipt || receipt.kind === "ordered-departure")
              add(
                "capability.departure-receipt",
                reqContext,
                "El recibo de salida debe ser un requisito existente que no dependa de otra salida",
              );
          } else if (req.receiptObjective === objective.id)
            add(
              "capability.departure-cycle",
              reqContext,
              "La salida no puede esperar el mismo objetivo que requiere esa salida; declare un recibo de requisito explícito",
            );
          break;
        case "phase-deadline":
          if (!phaseIds.has(req.phase))
            add(
              "capability.deadline-phase",
              reqContext,
              "Reloj asociado a fase inexistente",
            );
          if (
            !(
              Math.min(
                req.secondsByDifficulty.easy,
                req.secondsByDifficulty.standard,
                req.secondsByDifficulty.hard,
              ) > req.warningSeconds
            )
          )
            add(
              "capability.deadline-warning",
              reqContext,
              "El aviso debe preceder al vencimiento en todas las dificultades",
            );
          break;
      }
      for (const id of entityRefs)
        if (!entities.has(id))
          add(
            "capability.entity-reference",
            reqContext,
            `Entidad no declarada: ${id}`,
          );
      for (const id of zoneRefs)
        if (!zones.has(id))
          add(
            "capability.zone-reference",
            reqContext,
            `Zona no declarada: ${id}`,
          );
    }
    for (const exported of predicate.exportedLedgers ?? []) {
      if (exported.fromRequirements.some((id) => !reqIds.includes(id)))
        add(
          "capability.exported-ledger",
          context,
          "Un ledger exportado solo puede derivarse de predicados requeridos",
        );
    }
  }

  const phaseTransitionKeys = new Set<string>();
  for (const transition of profile.stateMachine.phaseTransitions) {
    const key = `${transition.from}->${transition.to}`;
    if (phaseTransitionKeys.has(key))
      add(
        "capability.phase-transition-duplicate",
        key,
        "Transición de fase duplicada",
      );
    phaseTransitionKeys.add(key);
    if (!phaseIds.has(transition.from) || !phaseIds.has(transition.to))
      add(
        "capability.phase-transition",
        key,
        "Transición enlaza una fase no declarada",
      );
    if (
      transition.on === "objective-latched" &&
      (!transition.objectiveId || !objectives.has(transition.objectiveId))
    )
      add(
        "capability.phase-transition-objective",
        key,
        "Transición requiere un objetivo existente",
      );
  }
  for (const objective of profile.objectivePlan) {
    if (
      !phaseTransitionKeys.has(`${objective.phase}->${objective.phase}`) &&
      !profile.stateMachine.phaseTransitions.some(
        (transition) => transition.to === objective.phase,
      )
    )
      add(
        "capability.phase-entry",
        objective.id,
        "La fase del objetivo no tiene una transición de entrada explícita",
      );
  }
  for (const [
    index,
    transition,
  ] of profile.stateMachine.transitions.entries()) {
    const match =
      /^(briefing|phase-[1-9][0-9]*|victory|defeat) → (briefing|phase-[1-9][0-9]*|victory|defeat)/.exec(
        transition,
      );
    if (
      !match ||
      !phaseIds.has(match[1] ?? "") ||
      !phaseIds.has(match[2] ?? "")
    )
      add(
        "capability.phase-transition",
        String(index),
        "Transición de fase con estado no declarado",
      );
  }
  const terminal = profile.stateMachine.states.filter(
    (state) => state === "victory" || state === "defeat",
  );
  if (terminal.length !== 2 || new Set(terminal).size !== 2)
    add(
      "capability.terminal-states",
      profile.profile,
      "Se requiere una sola victoria y una sola derrota terminal",
    );

  const sideEntities = new Map<
    string,
    (typeof profile.secondaryObjectives)[number]["world"]["entities"][number]
  >();
  const sideZones = new Map<
    string,
    (typeof profile.secondaryObjectives)[number]["world"]["zones"][number]
  >();
  const rewardFlags = new Set<string>();
  const costs = Object.fromEntries(resourceNames.map((r) => [r, 0])) as Record<
    (typeof resourceNames)[number],
    number
  >;
  const rewards = Object.fromEntries(
    resourceNames.map((r) => [r, 0]),
  ) as Record<(typeof resourceNames)[number], number>;
  for (const side of profile.secondaryObjectives) {
    if (side.mandatory || side.dependencies.length !== 0)
      add(
        "capability.secondary-optional",
        side.id,
        "Los secundarios son opcionales y no dependen de objetivos principales",
      );
    for (const entity of side.world.entities) {
      if (entities.has(entity.id) || sideEntities.has(entity.id))
        add(
          "capability.side-entity",
          entity.id,
          "Entidad secundaria no es exclusiva",
        );
      sideEntities.set(entity.id, entity);
      if (
        entity.initialHub !== side.reachability.originHub ||
        !districtIds.includes(entity.initialHub)
      )
        add(
          "capability.side-origin",
          entity.id,
          "Origen real distinto al contrato de alcance",
        );
    }
    for (const zone of side.world.zones) {
      if (zones.has(zone.id) || sideZones.has(zone.id))
        add("capability.side-zone", zone.id, "Zona secundaria no es exclusiva");
      sideZones.set(zone.id, zone);
      if (!districtIds.includes(zone.hub))
        add(
          "capability.side-zone-hub",
          zone.id,
          "Distrito secundario no declarado",
        );
    }
    const requirements = side.predicate.requirements;
    for (const req of requirements) {
      if (req.kind === "entity-arrival") {
        if (
          req.entities.some(
            (id) =>
              !sideEntities.has(id) &&
              !side.world.entities.some((entity) => entity.id === id),
          ) ||
          req.requiredCount > req.entities.length
        )
          add(
            "capability.side-arrival",
            side.id,
            "Llegada secundaria excede sus entidades finitas",
          );
        if (
          new Set(req.entities).size !== req.entities.length ||
          Object.keys(req.destinations).length !== req.entities.length
        )
          add(
            "capability.side-arrival-identity",
            side.id,
            "Cada llegada cuenta un ID una sola vez y tiene destino individual",
          );
        for (const [entityId, zoneId] of Object.entries(req.destinations)) {
          const entity = side.world.entities.find(
            (candidate) => candidate.id === entityId,
          );
          const zone = side.world.zones.find(
            (candidate) => candidate.id === zoneId,
          );
          if (!entity || !zone)
            add(
              "capability.side-destination",
              side.id,
              "Destino de llegada opcional no declarado",
            );
          else if (
            entity.initialHub === zone.hub &&
            Math.hypot(
              entity.offsetTiles[0] - zone.offsetTiles[0],
              entity.offsetTiles[1] - zone.offsetTiles[1],
            ) <= zone.radiusTiles
          )
            add(
              "capability.side-initial-arrival",
              entityId,
              "La posición inicial no cuenta como entrega",
            );
        }
      } else if (req.kind === "atomic-payment") {
        if (!req.once || !req.protectedRecoveryCannotBeSpent)
          add(
            "capability.side-payment",
            side.id,
            "Pago opcional debe ser único y respetar la reserva protegida",
          );
        if (receiptOwners.has(req.receipt))
          add("capability.receipt", req.receipt, "Recibo de pago reutilizado");
        receiptOwners.set(req.receipt, side.id);
        for (const resource of resourceNames)
          costs[resource] += req.resources[resource] ?? 0;
      } else if (req.kind === "visit-zones") {
        if (
          req.countInitialVisibility ||
          new Set(req.zones).size !== req.zones.length ||
          req.requiredCount !== req.zones.length ||
          req.zones.some(
            (id) => !side.world.zones.some((zone) => zone.id === id),
          )
        )
          add(
            "capability.side-visit",
            side.id,
            "La exploración exige visitar todos los destinos, no visibilidad inicial",
          );
      } else if (
        !side.world.entities.some((entity) => entity.id === req.entity) ||
        !requirements.some(
          (candidate) =>
            candidate.kind === "atomic-payment" &&
            candidate.receipt === req.paymentReceipt,
        )
      ) {
        add(
          "capability.side-repair",
          side.id,
          "Reparación debe referir su entidad finita y pago atómico",
        );
      }
    }
    for (const effect of side.effects) {
      if (rewardFlags.has(effect.onceFlag))
        add(
          "capability.reward-flag",
          effect.onceFlag,
          "Flag de recompensa reutilizado",
        );
      rewardFlags.add(effect.onceFlag);
      for (const resource of resourceNames)
        rewards[resource] += effect.resources[resource] ?? 0;
      if (effect.changesHistoricalOutcome)
        add(
          "capability.side-history",
          side.id,
          "Una recompensa no puede cambiar el desenlace histórico",
        );
    }
    if (
      side.stateContract.states.join(",") !==
        "available,completed,failed-optional,closed-at-terminal" ||
      !side.stateContract.persistentAcrossSave ||
      !side.stateContract.completionAndEffectsAtomic ||
      !side.stateContract.failedGoalCannotReward ||
      !side.stateContract.noMainVictoryDependency
    )
      add(
        "capability.side-state",
        side.id,
        "Estados secundarios deben ser persistentes, atómicos y opcionales",
      );
  }

  for (const resource of resourceNames) {
    if (
      (profile.secondaryBudget.reservedRewards[resource] ?? 0) !==
      rewards[resource]
    )
      add(
        "capability.reward-budget",
        resource,
        "Recompensas no corresponden al stock reservado",
      );
    if (
      rewards[resource] >
      (profile.secondaryBudget.reallocatedCacheAllowance[resource] ?? 0)
    )
      add(
        "capability.reward-allowance",
        resource,
        "Recompensa excede el antiguo banco opcional disponible",
      );
    if (
      costs[resource] >
      (profile.secondaryBudget.maxOptionalCosts[resource] ?? 0)
    )
      add(
        "capability.optional-cost-budget",
        resource,
        "Costes secundarios exceden el máximo presupuestado",
      );
  }

  const initial = new Set(profile.enemyRoster.initialEntityIds);
  if (initial.size !== profile.enemyRoster.initialEntityIds.length)
    add(
      "capability.enemy-roster",
      profile.profile,
      "Roster inicial contiene IDs repetidos",
    );
  for (const id of initial)
    if (!entities.has(id))
      add(
        "capability.enemy-roster-reference",
        id,
        "Unidad inicial no está en el worldContract finito",
      );
  const mobilized = new Set<string>();
  for (const wave of profile.enemyRoster.mobilizations) {
    for (const id of wave.entityIds) {
      if (!initial.has(id))
        add(
          "capability.enemy-wave-reference",
          wave.id,
          `Movilización crea unidad fuera del roster: ${id}`,
        );
      if (mobilized.has(id))
        add(
          "capability.enemy-wave-repeat",
          id,
          "Una unidad de reserva solo se moviliza una vez",
        );
      mobilized.add(id);
    }
  }
  const boundRosterIds = new Set<string>();
  for (const entity of entities.values())
    if (["military-guard", "military-post"].includes(entity.role)) {
      if (
        !entity.rosterSource ||
        entity.rosterSource !== "initialEnemy" ||
        !entity.rosterMemberId ||
        !initial.has(entity.rosterMemberId)
      )
        add(
          "capability.enemy-binding",
          entity.id,
          "La guarnición debe consumir un miembro del roster inicial",
        );
      if (entity.rosterMemberId && boundRosterIds.has(entity.rosterMemberId))
        add(
          "capability.enemy-binding-duplicate",
          entity.rosterMemberId,
          "Cada guarnición consume un miembro distinto del roster",
        );
      if (entity.rosterMemberId) boundRosterIds.add(entity.rosterMemberId);
    }
  if (profile.enemyRoster.productionEnabled)
    add(
      "capability.enemy-production",
      profile.profile,
      "Producción enemiga debe estar desactivada para el roster finito",
    );

  return [...out, ...validateRequirementCausality(profile)];
}

export function capabilityObjectiveRequirements(objective: MainObjective) {
  return objective.predicate.requirements;
}
