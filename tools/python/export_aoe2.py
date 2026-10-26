"""Puente de IR validado a AoE2ScenarioParser y rge_campaign. Sin formatos binarios propios."""
import argparse
import contextlib
import hashlib
import io
import json
import math
import os
from pathlib import Path
import runpy
import subprocess
import tempfile
import zipfile

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.trigger_lists import Comparison, Operation, DiplomacyState, Attribute
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.trigger_lists import VictoryCondition

ROOT = Path(__file__).resolve().parents[2]

_FACTORY = runpy.run_path(str(Path(__file__).resolve().parent / 'native_scenario.factory.py'))
enum_name = _FACTORY['enum_name']
unit_id = _FACTORY['unit_id']
create_native_scenario_base = _FACTORY['create_native_scenario_base']


def set_variable(trigger, variable, value):
    trigger.new_effect.change_variable(variable=variable, quantity=value, operation=Operation.SET)


def variable_is(trigger, variable, value):
    trigger.new_condition.variable_value(variable=variable, quantity=value, comparison=Comparison.EQUAL)


def apply_condition(trigger, condition, units, factions, variables):
    kind = condition['type']
    if kind == 'timer':
        trigger.new_condition.timer(timer=condition['seconds'])
    elif kind == 'destroy':
        trigger.new_condition.destroy_object(unit_object=units[condition['unit']])
    elif kind == 'variable':
        variable_is(trigger, variables[condition['variable']], condition['value'])
    elif kind == 'objective':
        variable_is(trigger, variables['objective-'+condition['objective']], 1)
    elif kind == 'bring':
        trigger.new_condition.bring_object_to_area(unit_object=units[condition['unit']], area_x1=condition['from']['x'], area_y1=condition['from']['y'], area_x2=condition['to']['x'], area_y2=condition['to']['y'])
    elif kind == 'resource':
        trigger.new_condition.accumulate_attribute(source_player=factions[condition['faction']]['player'], attribute=getattr(Attribute,condition['resource'].upper()+'_STORAGE'), quantity=condition['amount'])
    else:
        raise ValueError(f'Condición no soportada: {kind}')


def export_scenario(ir, out, version):
    if ir.get('schemaVersion') == 2 or ir.get('capability') or ir.get('scenario', {}).get('capabilityProfile'):
        raise ValueError('capability-not-implemented: composed-world-ledger schemaVersion 2 is reference-only; native Python export is deferred to i00003/S3')
    spec = ir['scenario']
    scenario, units, factions = create_native_scenario_base(ir, version)
    tm = scenario.trigger_manager
    variables = {'cdf-terminal': tm.add_variable('cdf-terminal').variable_id}
    for objective in spec['objectives']:
        variables[f"objective-{objective['id']}"] = tm.add_variable(f"objective-{objective['id']}").variable_id
    for var in spec['variables']:
        if var['id'] in variables:
            raise ValueError('Variable reservada')
        variables[var['id']] = tm.add_variable(var['id']).variable_id
    progress = tm.add_variable('cdf-progress-write').variable_id
    init = tm.add_trigger('cdf-initialize', enabled=True, looping=False)
    for name, index in variables.items():
        value = next((v['initial'] for v in spec['variables'] if v['id'] == name), 0)
        set_variable(init, index, value)
    for unit, string_id in ir.get('unitNameIds', {}).items():
        init.new_effect.change_object_name(selected_object_ids=units[unit], string_id=string_id)
    for faction, string_id in ir.get('factionNameIds', {}).items():
        init.new_effect.change_player_name(source_player=factions[faction]['player'], string_id=string_id)
    # XS usa comparaciones exactas/rangos de xsGetDifficulty, sin asumir el umbral de Difficulty Level.
    scenario.xs_manager.add_script(xs_string="\n".join([
        "bool cdfDifficultyEasy() { return (xsGetDifficulty() >= 3); }",
        "bool cdfDifficultyStandard() { return (xsGetDifficulty() == 2); }",
        "bool cdfDifficultyHard() { return (xsGetDifficulty() <= 1); }",
    ]))
    for profile, function in [('easy','cdfDifficultyEasy'),('standard','cdfDifficultyStandard'),('hard','cdfDifficultyHard')]:
        balance = spec['balance'][profile]
        setup = tm.add_trigger(f'cdf-balance-{profile}', enabled=True, looping=False)
        setup.new_condition.script_call(xs_function=function)
        if balance['hints'] and ir.get('messageIds', {}).get('hints'):
            setup.new_effect.display_instructions(source_player=1, string_id=ir['messageIds']['hints'], display_time=10)
        for resource, quantity in balance['resources'].items():
            setup.new_effect.modify_resource(source_player=1, tribute_list=getattr(Attribute, resource.upper()+'_STORAGE'), quantity=int(quantity), operation=Operation.SET)
        # Ordenar reservas iniciales después del tiempo de reacción elegido. No crear tropas.
        for faction in spec['factions']:
            if faction['role'] != 'enemy' or faction.get('aiScript'):
                continue
            action = tm.add_trigger(f"cdf-react-{profile}-{faction['id']}", enabled=True, looping=False)
            action.new_condition.script_call(xs_function=function)
            action.new_condition.timer(timer=balance['enemyReactionSeconds'])
            variable_is(action, variables['cdf-terminal'], 0)
            for unit in spec['units']:
                if unit['faction'] == faction['id']:
                    action.new_effect.task_object(selected_object_ids=units[unit['id']], location_x=spec['map']['start']['x'], location_y=spec['map']['start']['y'])
    for line in spec['narrative']['intro']:
        init.new_effect.display_instructions(string_id=ir['lineIds'][line['id']], source_player=1, display_time=max(1,math.ceil(line['durationSeconds'])))
    # Derrotas antes de objetivos/victoria; terminal guarda exclusión. El orden real requiere prueba en el juego.
    defeat_conditions = [('unit', name) for name in spec['defeat']['essentialUnits']]
    if spec['defeat'].get('timeoutSeconds'):
        defeat_conditions.append(('timeout', spec['defeat']['timeoutSeconds']))
    for kind, target in defeat_conditions:
        trigger = tm.add_trigger(f'cdf-defeat-{target}', enabled=True, looping=False)
        variable_is(trigger, variables['cdf-terminal'], 0)
        if kind == 'unit':
            trigger.new_condition.destroy_object(unit_object=units[target])
        else:
            trigger.new_condition.timer(timer=target)
        set_variable(trigger, variables['cdf-terminal'], 2)
        trigger.new_effect.declare_victory(source_player=1, enabled=0)
    for objective in spec['objectives']:
        trigger = tm.add_trigger(f"cdf-objective-{objective['id']}", enabled=True, looping=False, display_as_objective=True, description_stid=ir['objectiveIds'][objective['id']])
        variable_is(trigger, variables['cdf-terminal'], 0)
        for required in objective['requires']:
            variable_is(trigger, variables[f'objective-{required}'], 1)
        apply_condition(trigger, objective['completion'], units, factions, variables)
        set_variable(trigger, variables[f"objective-{objective['id']}"], 1)
    lines = {line['id']:line for line in spec['narrative']['events']}
    for event in spec.get('triggers', []):
        trigger = tm.add_trigger(f"cdf-event-{event['id']}", enabled=True, looping=False)
        variable_is(trigger, variables['cdf-terminal'], 0)
        for condition in event['conditions']:
            apply_condition(trigger, condition, units, factions, variables)
        for effect in event['effects']:
            kind=effect['type']
            if kind=='set-variable':
                set_variable(trigger,variables[effect['variable']],effect['value'])
            elif kind=='line':
                line=lines[effect['line']]
                trigger.new_effect.display_instructions(source_player=1,string_id=ir['lineIds'][line['id']],display_time=max(1,math.ceil(line['durationSeconds'])))
            elif kind=='task':
                trigger.new_effect.task_object(selected_object_ids=units[effect['unit']],location_object_reference=units[effect['target']])
            elif kind=='diplomacy':
                trigger.new_effect.change_diplomacy(source_player=factions[effect['source']]['player'], target_player=factions[effect['target']]['player'], diplomacy=getattr(DiplomacyState,effect['state'].upper()), mutual_diplomacy=effect['mutual'])
            elif kind=='tribute':
                trigger.new_effect.tribute(source_player=factions[effect['source']]['player'], target_player=factions[effect['target']]['player'], tribute_list=getattr(Attribute,effect['resource'].upper()+'_STORAGE'), quantity=effect['amount'])
            elif kind=='spawn':
                for _ in range(effect['count']):
                    trigger.new_effect.create_object(source_player=factions[effect['faction']]['player'],object_list_unit_id=unit_id(effect['unitType']),location_x=effect['position']['x'],location_y=effect['position']['y'])
            else:
                raise ValueError('Efecto de evento no soportado')
    routes=spec['victory'].get('routes',[])
    if not routes:
        routes=[{'id':'default','objectives':[], 'progressKey':spec['victory'].get('progressKey')}]
    for route in routes:
        win = tm.add_trigger(f"cdf-victory-{route['id']}", enabled=True, looping=False)
        variable_is(win, variables['cdf-terminal'], 0)
        for target in dict.fromkeys(spec['victory']['objectives']+route['objectives']):
            variable_is(win, variables[f'objective-{target}'], 1)
        set_variable(win, variables['cdf-terminal'], 1)
        if route.get('progressKey'):
            set_variable(win, progress, 1)
            win.new_effect.store_key_value(variable=progress, message=route['progressKey'])
        win.new_effect.declare_victory(source_player=1, enabled=1)
    scenario.write_to_file(str(out))
    reopened = AoE2DEScenario.from_file(str(out))
    if reopened.scenario_version != version or len(reopened.trigger_manager.triggers) != len(tm.triggers):
        raise RuntimeError('Round-trip del escenario falló')
    def signature(trigger):
        condition_fields=['condition_type','quantity','variable','comparison','unit_object','timer','xs_function','source_player','attribute','area_x1','area_y1','area_x2','area_y2']
        effect_fields=['effect_type','quantity','variable','operation','source_player','string_id','display_time','message','location_x','location_y','location_object_reference','object_list_unit_id','enabled','tribute_list','target_player','diplomacy','mutual_diplomacy','selected_object_ids']
        return (trigger.name,trigger.enabled,trigger.looping,
                [[getattr(c,n,None) for n in condition_fields] for c in trigger.conditions],
                [[getattr(e,n,None) for n in effect_fields] for e in trigger.effects])
    if [signature(t) for t in reopened.trigger_manager.triggers] != [signature(t) for t in tm.triggers]:
        raise RuntimeError('Round-trip alteró condiciones/efectos de disparadores')
    if [(t.terrain_id, t.elevation) for t in reopened.map_manager.terrain] != [(t.terrain_id, t.elevation) for t in scenario.map_manager.terrain]:
        raise RuntimeError('Round-trip alteró terreno/elevación')
    for field, string_id in ir.get('messageIds', {}).items():
        if getattr(reopened.message_manager, field+'_string_table_id') != string_id:
            raise RuntimeError('Round-trip alteró panel localizado')
    if reopened.option_manager.victory_condition != VictoryCondition.CUSTOM:
        raise RuntimeError('Victoria personalizada no persistida')
    return {'id': spec['id'], 'sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'triggers': len(tm.triggers), 'units': len(spec['units']), 'version': version}


def rge_binary():
    override = os.environ.get('RGE_CAMPAIGN_BIN')
    if override:
        return Path(override).resolve()
    commit = json.loads((ROOT/'config/toolchain.json').read_text())['commit']
    path = ROOT/'.cache/toolchain'/commit/('rge_campaign.exe' if os.name == 'nt' else 'rge_campaign')
    if not path.is_file():
        raise RuntimeError('Falta rge_campaign. Ejecuta python tools/python/setup.py')
    return path


def build(ir_path, output):
    ir = json.loads(ir_path.read_text(encoding='utf8'))
    if ir.get('schemaVersion') == 2 or any(s.get('schemaVersion') == 2 or s.get('capability') or s.get('scenario', {}).get('capabilityProfile') for s in ir.get('scenarios', [])):
        raise ValueError('capability-not-implemented: composed-world-ledger schemaVersion 2 is reference-only; native Python export is deferred to i00003/S3')
    if ir['mode'] != 'aoe2-de':
        raise ValueError('Return of Rome pendiente de experimento, exportación rechazada')
    config = json.loads((ROOT/'config/engine.json').read_text())
    version = config['scenarioVersion']
    output.mkdir(parents=True, exist_ok=True)
    files = []
    reports = []
    with contextlib.redirect_stdout(io.StringIO()):
        for spec in ir['scenarios']:
            path = output/f"{spec['scenario']['id']}.aoe2scenario"
            reports.append(export_scenario(spec, path, version))
            files.append(path)
    target = output/f"{ir['internalName']}.aoe2campaign"
    binary = rge_binary()
    subprocess.run([str(binary),'c',str(target),ir['internalName'],*[str(p) for p in files]], check=True, capture_output=True)
    with tempfile.TemporaryDirectory() as tmp:
        extracted = Path(tmp)/'extracted'
        subprocess.run([str(binary),'x',str(target),str(extracted)], check=True, capture_output=True)
        recovered = list(extracted.rglob('*.aoe2scenario'))
        if len(recovered)!=len(files) or sorted(hashlib.sha256(p.read_bytes()).hexdigest() for p in recovered)!=sorted(r['sha256'] for r in reports):
            raise RuntimeError('Round-trip contenedor no preserva escenarios')
    report={'status':'EXPORT READY (binary subset)','campaignSha256':hashlib.sha256(target.read_bytes()).hexdigest(),'scenarioReports':reports,'gameVerified':False,'pending':['slideshow-layout','difficulty-runtime','multi-mod-localization','save-load-progression','audio-engine-paths']}
    (output/'export-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    return report


def zip_package(source, target):
    # Fechas y orden fijos; nunca empaquetar enlaces ni el reporte privado de producción.
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob('*')):
            if path.is_symlink():
                raise ValueError('Enlace no permitido en mod')
            if not path.is_file():
                continue
            name = path.relative_to(source).as_posix()
            info=zipfile.ZipInfo(name,date_time=(2020,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644 << 16
            archive.writestr(info,path.read_bytes())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['build','zip','catalog'])
    parser.add_argument('input',type=Path,nargs='?')
    parser.add_argument('output',type=Path,nargs='?')
    args=parser.parse_args()
    if args.action=='catalog':
        print(json.dumps({'civilizations':[c.name.lower().replace('_','-') for c in Civilization], 'units':[u.name.lower().replace('_','-') for u in UnitInfo], 'buildings':[u.name.lower().replace('_','-') for u in BuildingInfo], 'technologies':[t.name.lower().replace('_','-') for t in TechInfo], 'terrains':[t.name.lower().replace('_','-') for t in TerrainId]}))
    elif args.action=='build':
        print(json.dumps(build(args.input,args.output)))
    else:
        zip_package(args.input,args.output)

if __name__=='__main__':
    main()
