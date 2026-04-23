from configuration.config import config
from function.util import checkIfExist
from handles.manager_void import manager_void

def m_void(dlg, action):

    action_cfg = getattr(config, action, None)
    if action_cfg is None:
        print(f"No config found for action: {action}")
        return

    sequences = getattr(action_cfg, "sequence", [])
    
    for sequence in sequences:       
        manager_void(dlg, **vars(sequence))

