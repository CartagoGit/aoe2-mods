"""Base nativa compartida: mapa, jugadores, unidades iniciales y muros bloqueados.

Extrae del exportador legado la parte ya implementada del escenario nativo para
que un llamador futuro reutilice la misma base. Solo construye la envoltura
base: objetivos, fases, reacciones, texto de disparadores, progreso, XS y
escritura final siguen en el exportador legado. La base admite únicamente una
envoltura schemaVersion 1; la presencia de cualquier metadato de capacidad
(capability, scenario.capability o scenario.capabilityProfile) se rechaza aunque
esté vacío o nulo, y una envoltura compuesta o desconocida no se degrada a v1.
"""
import os
import sys

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState, VictoryCondition


def enum_name(name):
    return name.upper().replace('-', '_')


def unit_id(name):
    key = enum_name(name)
    for dataset in (UnitInfo, BuildingInfo):
        if hasattr(dataset, key):
            return getattr(dataset, key).ID
    raise ValueError(f'Unidad no soportada: {name}')


def _reject_unknown_envelope(ir):
    if not isinstance(ir, dict) or type(ir.get('schemaVersion')) is not int or ir.get('schemaVersion') != 1:
        raise ValueError('native-base-unsupported: la base nativa solo admite una envoltura schemaVersion 1')
    spec = ir.get('scenario')
    if not isinstance(spec, dict):
        raise ValueError('native-base-unsupported: la envoltura nativa exige un escenario declarado')
    for owner, name in ((ir, 'capability'), (spec, 'capability'), (spec, 'capabilityProfile')):
        if name in owner:
            raise ValueError(f'native-base-unsupported: la base nativa no admite el metadato de capacidad "{name}"')


def create_native_scenario_base(ir, version):
    """Construye la base nativa de un escenario v1: (scenario, units, factions)."""
    _reject_unknown_envelope(ir)
    spec = ir['scenario']
    if spec['map']['width'] != spec['map']['height']:
        raise ValueError('Perfil AoE2: mapa cuadrado obligatorio')
    for faction in spec['factions']:
        if faction['role'] != 'human' and faction['economy']['model'] != 'finite-reserve' and not faction.get('aiScript'):
            raise ValueError('IA económica/guionizada exige aiScript PER explícito; no se sustituye por oleadas')
    scenario = AoE2DEScenario.from_default(version)
    if os.environ.get('COF_XS_CHECK_BIN'):
        scenario.xs_manager.xs_check.path = os.environ['COF_XS_CHECK_BIN']
    elif sys.platform == 'darwin':
        raise RuntimeError('Exportar en macOS exige COF_XS_CHECK_BIN compatible (0.1.2–0.2.30); el wheel incluye ELF Linux. Ver guía de desarrollo.')
    scenario.xs_manager.xs_check.raise_on_error = True
    scenario.map_manager.map_size = spec['map']['width']
    base = getattr(TerrainId, enum_name(spec['map']['baseTerrain']))
    for tile in scenario.map_manager.terrain:
        tile.terrain_id = int(base)
    for tile in spec['map']['tiles']:
        cell = scenario.map_manager.get_tile(tile['position']['x'], tile['position']['y'])
        cell.terrain_id = int(getattr(TerrainId, enum_name(tile['terrain'])))
        cell.elevation = tile['elevation']
    for field, string_id in ir.get('messageIds', {}).items():
        setattr(scenario.message_manager, field, '')
        setattr(scenario.message_manager, field+'_string_table_id', string_id)
    scenario.option_manager.victory_condition = VictoryCondition.CUSTOM
    scenario.option_manager.victory_custom_conditions_required = True
    scenario.option_manager.lock_teams = True
    scenario.option_manager.allow_players_choose_teams = False
    factions = {f['id']: f for f in spec['factions']}
    slots = sorted(f['player'] for f in spec['factions'])
    if slots != list(range(1, max(slots)+1)):
        raise ValueError('Slots activos deben ser consecutivos')
    scenario.player_manager.active_players = max(slots)
    for faction in spec['factions']:
        player = scenario.player_manager.players[faction['player']]
        player.human = faction['role'] == 'human'
        player.civilization = getattr(Civilization, enum_name(faction['civilization']))
        player.lock_civ = True
        player.lock_personality = True
        player.population_cap = 200
        if faction['role'] != 'human':
            if faction.get('aiScript'):
                player.set_custom_ai(faction['id'], ai_script=faction['aiScript'])
            else:
                player.set_none_ai()
        if spec['technologies']:
            allowed = {getattr(TechInfo, enum_name(t)).ID for t in spec['technologies']}
            player.disabled_techs = sorted({t.ID for t in TechInfo if t.ID >= 0} - allowed)
        player.initial_player_view_x = spec['map']['start']['x']
        player.initial_player_view_y = spec['map']['start']['y']
        for resource, value in faction['economy']['initial'].items():
            setattr(player, resource, int(value))
        for other in spec['factions']:
            state = DiplomacyState.ALLY if other['role'] != 'enemy' and faction['role'] != 'enemy' else DiplomacyState.ENEMY
            player.diplomacy[other['player']] = int(state)
    units = {}
    for unit in spec['units']:
        obj = scenario.unit_manager.add_unit(player=factions[unit['faction']]['player'], unit_const=unit_id(unit['type']), x=unit['position']['x']+0.5, y=unit['position']['y']+0.5)
        units[unit['id']] = obj.reference_id
    for p in spec['map']['blocked']:
        scenario.unit_manager.add_unit(player=0, unit_const=BuildingInfo.STONE_WALL.ID, x=p['x']+0.5, y=p['y']+0.5)
    return scenario, units, factions
