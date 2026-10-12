import { duplicates, type Issue, issue } from "../core";
import type { Campaign, Scenario } from "../schemas";
export function reachable(s: Scenario): Set<string> {
  const blocked = new Set(s.map.blocked.map((p) => `${p.x},${p.y}`));
  const seen = new Set<string>();
  const queue = [s.map.start];
  for (let i = 0; i < queue.length; i++) {
    const p = queue[i];
    if (!p) continue;
    const k = `${p.x},${p.y}`;
    if (
      p.x < 0 ||
      p.y < 0 ||
      p.x >= s.map.width ||
      p.y >= s.map.height ||
      blocked.has(k) ||
      seen.has(k)
    )
      continue;
    seen.add(k);
    queue.push(
      { x: p.x + 1, y: p.y },
      { x: p.x - 1, y: p.y },
      { x: p.x, y: p.y + 1 },
      { x: p.x, y: p.y - 1 },
    );
  }
  return seen;
}
export function validateGameplay(s: Scenario): Issue[] {
  const out: Issue[] = [];
  const units = new Map(s.units.map((u) => [u.id, u]));
  const factions = new Map(s.factions.map((f) => [f.id, f]));
  const objectives = new Map(s.objectives.map((o) => [o.id, o]));
  const vars = new Set(s.variables.map((v) => v.id));
  for (const [kind, ids] of [
    ["unit", s.units.map((u) => u.id)],
    ["objective", s.objectives.map((o) => o.id)],
    ["faction", s.factions.map((f) => f.id)],
    ["variable", s.variables.map((v) => v.id)],
  ] as const)
    for (const id of duplicates([...ids]))
      out.push(issue(`game.${kind}-duplicate`, id, "ID repetido"));
  if (
    s.factions.filter((f) => f.role === "human").length !== 1 ||
    s.factions.find((f) => f.role === "human")?.player !== 1
  )
    out.push(
      issue(
        "game.human",
        s.id,
        "El perfil actual exige un jugador humano en slot 1",
      ),
    );
  if (new Set(s.factions.map((f) => f.player)).size !== s.factions.length)
    out.push(issue("game.player", s.id, "Slot de jugador repetido"));
  for (const position of duplicates(
    s.map.tiles.map((t) => `${t.position.x},${t.position.y}`),
  ))
    out.push(issue("game.tile-duplicate", position, "Tesela repetida"));
  const reached = reachable(s);
  const points = [
    s.map.start,
    ...s.map.blocked,
    ...s.map.tiles.map((t) => t.position),
    ...s.units.map((u) => u.position),
    ...s.objectives.map((o) => o.location),
  ];
  for (const p of points)
    if (p.x >= s.map.width || p.y >= s.map.height)
      out.push(
        issue("game.bounds", s.id, `Coordenadas fuera del mapa ${p.x},${p.y}`),
      );
  for (const o of s.objectives) {
    if (!reached.has(`${o.location.x},${o.location.y}`))
      out.push(
        issue(
          "game.connectivity",
          o.id,
          "Objetivo inaccesible en la cuadrícula abstracta",
        ),
      );
    for (const dep of o.requires)
      if (!objectives.has(dep))
        out.push(
          issue("game.dependency", o.id, `Objetivo inexistente: ${dep}`),
        );
    if (o.completion.type === "destroy" && !units.has(o.completion.unit))
      out.push(issue("game.unit", o.id, "Unidad objetivo inexistente"));
    if (o.completion.type === "variable" && !vars.has(o.completion.variable))
      out.push(issue("game.variable", o.id, "Variable no inicializada"));
  }
  const conditions = [
    ...s.objectives.map((o) => o.completion),
    ...s.triggers.flatMap((t) => t.conditions),
  ];
  for (const cond of conditions) {
    if (cond.type === "bring") {
      if (!units.has(cond.unit))
        out.push(issue("game.area-unit", s.id, "Unidad del área inexistente"));
      if (
        cond.from.x > cond.to.x ||
        cond.from.y > cond.to.y ||
        cond.to.x >= s.map.width ||
        cond.to.y >= s.map.height
      )
        out.push(
          issue("game.area-bounds", s.id, "Rectángulo de llegada inválido"),
        );
    }
    if (cond.type === "resource" && !factions.has(cond.faction))
      out.push(
        issue("game.resource-faction", s.id, "Facción de recursos inexistente"),
      );
  }
  const eventLines = new Set(s.narrative.events.map((l) => l.id));
  const reserved = new Set([
    "cdf-terminal",
    "cdf-progress-write",
    "cdf-enemy-reaction",
  ]);
  for (const v of s.variables)
    if (reserved.has(v.id) || v.id.startsWith("objective-"))
      out.push(
        issue("game.reserved", v.id, "Variable reservada por el compilador"),
      );
  if (s.variables.length + s.objectives.length + 3 > 256)
    out.push(
      issue(
        "game.variable-limit",
        s.id,
        "El perfil del parser admite 256 variables",
      ),
    );
  const waves = new Map<string, { count: number; units: number }>();
  const delivered = new Set<string>();
  for (const t of s.triggers) {
    for (const cond of t.conditions) {
      if (cond.type === "variable" && !vars.has(cond.variable))
        out.push(
          issue(
            "game.event-variable",
            t.id,
            "Variable de condición inexistente",
          ),
        );
      if (cond.type === "destroy" && !units.has(cond.unit))
        out.push(
          issue("game.event-unit", t.id, "Unidad de condición inexistente"),
        );
      if (cond.type === "objective" && !objectives.has(cond.objective))
        out.push(
          issue(
            "game.event-objective",
            t.id,
            "Objetivo de condición inexistente",
          ),
        );
    }
    for (const e of t.effects) {
      if (e.type === "diplomacy" || e.type === "tribute") {
        if (
          !factions.has(e.source) ||
          !factions.has(e.target) ||
          e.source === e.target
        )
          out.push(
            issue(
              "game.event-factions",
              t.id,
              "Facciones de efecto inexistentes o iguales",
            ),
          );
        if (e.type === "tribute") {
          const total = t.effects
            .filter(
              (x) =>
                x.type === "tribute" &&
                x.source === e.source &&
                x.resource === e.resource,
            )
            .reduce((sum, x) => sum + (x.type === "tribute" ? x.amount : 0), 0);
          if (
            !t.conditions.some(
              (c) =>
                c.type === "resource" &&
                c.faction === e.source &&
                c.resource === e.resource &&
                c.amount >= total,
            )
          )
            out.push(
              issue(
                "game.tribute-budget",
                t.id,
                "Tributo necesita condición de saldo suficiente para su coste total",
              ),
            );
        }
      }
      if (e.type === "set-variable" && !vars.has(e.variable))
        out.push(
          issue("game.event-variable", t.id, "Variable de efecto inexistente"),
        );
      if (e.type === "line") {
        delivered.add(e.line);
        if (!eventLines.has(e.line))
          out.push(issue("game.event-line", t.id, "Línea inexistente"));
      }
      if (e.type === "task" && (!units.has(e.unit) || !units.has(e.target)))
        out.push(
          issue("game.event-unit", t.id, "Orden con unidades inexistentes"),
        );
      if (e.type === "spawn") {
        const faction = factions.get(e.faction);
        const reserve = faction?.reinforcements.find(
          (r) => r.id === e.reinforcement,
        );
        if (!reserve)
          out.push(
            issue(
              "game.event-reserve",
              t.id,
              "Reserva no declarada para esta facción",
            ),
          );
        const k = `${e.faction}.${e.reinforcement}`;
        const prev = waves.get(k) ?? { count: 0, units: 0 };
        waves.set(k, { count: prev.count + 1, units: prev.units + e.count });
        if (reserve && e.count > reserve.unitsPerWave)
          out.push(
            issue(
              "game.event-budget",
              t.id,
              "Oleada supera unidades autorizadas",
            ),
          );
        if (!reached.has(`${e.position.x},${e.position.y}`))
          out.push(issue("game.event-spawn", t.id, "Refuerzo inaccesible"));
      }
    }
  }
  for (const line of eventLines)
    if (!delivered.has(line))
      out.push(
        issue("game.event-unbound", line, "Línea sin evento que la active"),
      );
  for (const [k, total] of waves) {
    const [faction, id] = k.split(".");
    const reserve = factions
      .get(faction ?? "")
      ?.reinforcements.find((r) => r.id === id);
    if (
      reserve &&
      (total.count > reserve.maxWaves || total.units > reserve.totalBudget)
    )
      out.push(issue("game.event-budget", k, "Eventos exceden reserva total"));
  }
  const active = new Set<string>();
  const done = new Set<string>();
  const visit = (id: string): void => {
    if (active.has(id)) {
      out.push(issue("game.cycle", id, "Ciclo de objetivos"));
      return;
    }
    if (done.has(id)) return;
    active.add(id);
    for (const dep of objectives.get(id)?.requires ?? []) visit(dep);
    active.delete(id);
    done.add(id);
  };
  for (const o of s.objectives) visit(o.id);
  for (const id of s.victory.objectives)
    if (!objectives.has(id))
      out.push(issue("game.victory", id, "Objetivo final desconocido"));
  for (const route of s.victory.routes)
    for (const target of route.objectives)
      if (!objectives.has(target))
        out.push(
          issue(
            "game.route-objective",
            route.id,
            "Objetivo de ruta inexistente",
          ),
        );
  for (const duplicate of duplicates(s.victory.routes.map((r) => r.id)))
    out.push(issue("game.route-id", duplicate, "Ruta duplicada"));
  for (const duplicate of duplicates(
    s.victory.routes.map((r) => r.progressKey),
  ))
    out.push(issue("game.route-key", duplicate, "Cada ruta necesita su clave"));
  for (const id of s.defeat.essentialUnits)
    if (!units.has(id) || !units.get(id)?.essential)
      out.push(issue("game.defeat", id, "Unidad crítica ausente o sin marcar"));
  for (const u of s.units) {
    if (!factions.has(u.faction))
      out.push(issue("game.faction", u.id, "Facción inexistente"));
    if (!reached.has(`${u.position.x},${u.position.y}`))
      out.push(issue("game.spawn", u.id, "Unidad atrapada en cuadrícula"));
  }
  for (const f of s.factions)
    for (const r of f.reinforcements)
      if (r.maxWaves * r.unitsPerWave > r.totalBudget)
        out.push(
          issue("game.reserve", r.id, "Refuerzos exceden la reserva finita"),
        );
  if (
    s.balance.easy.enemyReactionSeconds <
      s.balance.standard.enemyReactionSeconds ||
    s.balance.standard.enemyReactionSeconds <
      s.balance.hard.enemyReactionSeconds
  )
    out.push(
      issue(
        "game.balance",
        s.id,
        "La reacción debe acelerar con la dificultad",
      ),
    );
  if (s.metrics.durationMinutes[0] > s.metrics.durationMinutes[1])
    out.push(issue("game.metrics", s.id, "Intervalo de duración invertido"));
  return out;
}
export function validateVariety(c: Campaign): Issue[] {
  const out: Issue[] = [];
  for (let i = 2; i < c.scenarios.length; i++)
    if (
      c.scenarios[i]?.mechanic === c.scenarios[i - 1]?.mechanic &&
      c.scenarios[i]?.mechanic === c.scenarios[i - 2]?.mechanic
    )
      out.push(
        issue(
          "game.repetition",
          c.scenarios[i]?.id ?? c.id,
          "Tres mecánicas principales consecutivas iguales",
          "warning",
        ),
      );
  return out;
}
