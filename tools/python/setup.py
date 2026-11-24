"""Instala herramientas aisladas; descarga rge_campaign fijado sin incorporarlo al repo."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request
import venv

ROOT = Path(__file__).resolve().parents[2]

def run(args):
    subprocess.run(args, check=True, cwd=ROOT)

def main():
    directory = ROOT / '.venv'
    if not directory.exists():
        venv.create(directory, with_pip=True)
    interpreter = directory / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    run([str(interpreter), '-m', 'pip', 'install', '--require-hashes', '-r', str(ROOT / 'requirements.lock.txt')])
    if os.name != 'nt':
        # El wheel incluye xs-check sin permiso de ejecución en algunas instalaciones Unix.
        code = "import AoE2ScenarioParser; from pathlib import Path; p=Path(AoE2ScenarioParser.__file__).parent/'dependencies/xs-check/xs-check'; p.chmod(p.stat().st_mode | 0o100)"
        run([str(interpreter), '-c', code])
    if os.environ.get('RGE_CAMPAIGN_BIN'):
        return
    config = json.loads((ROOT / 'config/toolchain.json').read_text())
    cache = ROOT / '.cache/toolchain' / config['commit']
    cache.mkdir(parents=True, exist_ok=True)
    for name, expected in config['files'].items():
        path = cache / name
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            url = f"https://raw.githubusercontent.com/withmorten/rge_campaign/{config['commit']}/{name}"
            with urllib.request.urlopen(url, timeout=30) as response:
                content = response.read()
            if hashlib.sha256(content).hexdigest() != expected:
                raise RuntimeError(f'Hash inesperado: {name}')
            path.write_bytes(content)
    compiler = next((shutil.which(c) for c in ['cc', 'gcc', 'clang'] if shutil.which(c)), None)
    if not compiler:
        raise RuntimeError('Falta compilador C o RGE_CAMPAIGN_BIN; ver docs/guides/development.md')
    target = cache / ('rge_campaign.exe' if os.name == 'nt' else 'rge_campaign')
    run([compiler, '-O2', '-o', str(target), str(cache/'main.c'), str(cache/'util.c')])
    print(f'Herramientas instaladas: {interpreter}, {target}')

if __name__ == '__main__':
    main()
