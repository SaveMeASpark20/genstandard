from configuration.config import config
from function.util import checkIfExist
from procedure.openautomate import openautomate

def open_auto(dlg, action):

    action_cfg = getattr(config, action, None)
    if action_cfg is None:
        print(f"No config found for action: {action}")
        return

    sequences = getattr(action_cfg, "sequence", [])

    for sequence in sequences:        
        openautomate(dlg, action, **vars(sequence))

