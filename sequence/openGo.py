import subprocess
import os
import time
from pywinauto import Application
from pywinauto.findwindows import find_elements
from configuration.config import config

def openGo(is_OTK=False, backend="uia"):
    pos_no = config.OTK if is_OTK else config.POS
    bat_path = config.go_bat_loc_OTK if is_OTK else config.go_bat_loc
    work_dir = os.path.dirname(bat_path)

    print(f"Launching GO.BAT → {'OTK' if is_OTK else 'POS'}: {bat_path}")
    subprocess.Popen(['start', 'cmd.exe', '/k', bat_path], shell=True, cwd=work_dir)


    print("⏳ Waiting for main app window...")

    for count in range(30):
        print(f"⏱️  Waiting... {count + 1}s")
        windows = find_elements(title_re=".*W I N V Q P.*", control_type="Window", backend=backend)

        for elem in windows:
            try:
                app = Application(backend=backend).connect(handle=elem.handle)
                dlg = app.window(handle=elem.handle)
                if dlg.child_window(title=pos_no, control_type="Text").exists():
                    print("✅ WINVQP is running!")
                    return dlg
            except Exception as e:
                print(f"⚠️ Error connecting: {e}")
        
        time.sleep(1)

    print("❌ App window not found after 30s.")
    return None
