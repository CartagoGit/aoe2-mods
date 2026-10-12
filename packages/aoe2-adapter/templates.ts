import type { StringLock } from "../localization";

/** Solo transforma una plantilla nativa obtenida del editor/juego y documentada; no inventa su envoltura. */
export function bindNativeTemplate(
  template: unknown,
  strings: StringLock,
  values: Record<string, string | number>,
): unknown {
  const bind = (value: unknown): unknown => {
    if (Array.isArray(value)) return value.map(bind);
    if (value !== null && typeof value === "object")
      return Object.fromEntries(
        Object.entries(value).map(([k, v]) => [k, bind(v)]),
      );
    if (typeof value !== "string") return value;
    if (value.startsWith("@cdf:string:")) {
      const key = value.slice(12);
      const id = strings.ids[key];
      if (id === undefined)
        throw new Error(`Plantilla: clave desconocida ${key}`);
      return id;
    }
    if (value.startsWith("@cdf:value:")) {
      const name = value.slice(11);
      const result = values[name];
      if (result === undefined)
        throw new Error(`Plantilla: valor desconocido ${name}`);
      return result;
    }
    return value;
  };
  return bind(template);
}
export function progressCondition(
  campaign: string,
  key: string,
  incomplete: boolean,
) {
  return {
    Type: "CampaignVariable",
    Campaign: campaign,
    Key: key,
    Comparison: incomplete ? "<=0" : ">0",
  } as const;
}
