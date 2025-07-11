import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from sequence.managerSignon import managerSignon
from sequence.openGo import openGo
from configuration.config import config
from transaction.dinein import bacchusDineIn
from sequence.cashierSignon import cashierSignon
from pywinauto.findwindows import find_elements
from function.clickButton import clickBtn



def main(backend="uia"):
    try:
        windows = find_elements(title_re=".*" +  "W I N V Q P" + ".*", control_type="Window", backend="uia")
        app1, app2 = None, None
        dlg1, dlg2 = None, None
        
        if windows is None:
            dlg1 = openGo()
        for elem in windows:
            app = Application(backend="uia").connect(handle=elem.handle)
            dlg = app.window(handle=elem.handle)

            if dlg.child_window(title="01", control_type="Text").exists():
                app1 = app
                
                print("Identified App 1 (with '01')")
            elif dlg.child_window(title="T1", control_type="Text").exists():
                app2 = app
                print("Identified App 2 (with 'T1')")

        dlg1 = app1.window(title_re=".*" + "W I N V Q P" + ".*")

        if(app2):
            dlg2 = app2.window(title_re=".*" + "W I N V Q P" + ".*")

    except ElementNotFoundError:
        if dlg1 is None:
            dlg1 = openGo()

        
    clickBtn(dlg1, 'DINE IN')
    
    if dlg2 is None:
        dlg2 = openGo(is_OTK=True)
        managerSignon(dlg2)
        clickBtn(dlg2, 'DINE IN')
    

if __name__ == "__main__":
    main()

    
