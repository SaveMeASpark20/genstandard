import subprocess
import os
import time
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError

from configuration.config import config

def openGo():
    bat_path = config.go_bat_loc
    work_dir = os.path.dirname(bat_path)

    subprocess.Popen(['cmd.exe', '/c', 'start', '', bat_path], cwd=work_dir, shell=True)

    print("Waiting for main app window...")

    app = Application(backend="uia")
    for _ in range(30):  # wait up to 30 seconds
        try:
            app.connect(title_re=".*W I N V Q P.*") 
            main_dlg = app.window(title_re=".*W I N V Q P.*")
            print("WINVQP RUNNING!")
            return main_dlg
        except ElementNotFoundError:
            time.sleep(1)

    print("App window not found.")
    return None

