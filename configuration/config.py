
"""
    The function `dict_to_namespace` converts a dictionary into a namespace object in Python.
    
    :param d: The parameter `d` in the `dict_to_namespace` function represents the dictionary or list
    that is being converted into a namespace object. The function recursively converts nested
    dictionaries and lists into namespace objects using the `SimpleNamespace` class from the `types`
    module
    :return: The code snippet provided is reading a JSON configuration file named `config.json` located
    next to the main executable file (assuming the script is frozen into an executable). The contents of
    the JSON file are loaded and converted into a namespace object using the `dict_to_namespace`
    function defined in the code.
"""
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
