import os
import sys
import json
from types import SimpleNamespace

def dict_to_namespace(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(i) for i in d]
    return d

def get_executable_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)  # .exe mode
    return os.path.dirname(os.path.abspath(__file__))  # dev mode

# This assumes config.json is next to the main.exe
config_path = os.path.join(get_executable_dir(), 'config.json')

with open(config_path, 'r', encoding='utf-8') as f:
    config_data = json.load(f)

config = dict_to_namespace(config_data)
