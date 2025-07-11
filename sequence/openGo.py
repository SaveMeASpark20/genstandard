import subprocess
import os
import time
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.findwindows import find_elements
from configuration.config import config

def openGo(is_OTK=False):
    pos_no = None
    if is_OTK:
        bat_path = config.go_bat_loc_OTK
        pos_no = config.POS
    else :
        bat_path = config.go_bat_loc
        pos_no = config.OTK
        
    work_dir = os.path.dirname(bat_path)

    subprocess.Popen(['cmd.exe', '/c', 'start', '', bat_path], cwd=work_dir, shell=True)

    print("Waiting for main app window...")
    windows = find_elements(title_re=".*" +  "W I N V Q P" + ".*", control_type="Window", backend="uia")
    
    for _ in range(30):  # wait up to 30 seconds
        try:
            for elem in windows:
                app= Application(backend="uia").connect(handle=elem.handle) 
                dlg = app.window(handle=elem.handle)
                if dlg.child_window(title=pos_no, control_type="Text").exists():
                    return dlg
                
        except ElementNotFoundError:
            time.sleep(1)

    print("App window not found.")
    return None

