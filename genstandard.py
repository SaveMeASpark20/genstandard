import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from sequence.managerSignon import managerSignon
from sequence.openGo import openGo
from configuration.config import config
from transaction.dinein import bacchusDineIn
from transaction.dinein import bacchusDineInOTK
from transaction.takeout import bacchusTakeOut
from transaction.takeout import bacchusTakeOutOTK
from transaction.delivery import delivery
from transaction.bulk import bulk
from sequence.cashierSignon import cashierSignon
from handles.tender_amount import tender_amount
from pywinauto.findwindows import find_elements
from function.clickButton import clickBtn
from function.util import checkIfExist
from handles.open_reg import open_reg
from sequence.backMgrMenu import clickBckMgrMenu
from configuration.config import config
import time



def main(backend="uia"):
    pos_no = config.POS
    otk_no = config.OTK

    dlg1, dlg2 = None, None

    # Step 1: Scan open windows
    windows = find_elements(title_re=".*W I N V Q P.*", control_type="Window", backend=backend)

    for elem in windows:
        app = Application(backend=backend).connect(handle=elem.handle)
        dlg = app.window(handle=elem.handle)

        if dlg.child_window(title=pos_no, control_type="Text").exists():
            dlg1 = dlg
            print("✅ Identified App1 (POS)")

        elif dlg.child_window(title=otk_no, control_type="Text").exists():
            dlg2 = dlg
            print("✅ Identified App2 (OTK)")

    # Step 2: Open main POS window if not found
    if dlg1 is None:
        print("⚠️ POS window not found, launching...")
        dlg1 = openGo()
        dlg1.set_focus()
        managerSignon(dlg1)
        cashierSignon(dlg1)


    if dlg2 is None:
        print("ℹ️ OTK window not found, launching...")
        dlg2 = openGo(is_OTK=True)
        dlg2.set_focus()
        managerSignon(dlg2)
        open_reg(dlg2)
        cashierSignon(dlg2)

    time.sleep(5)
    bacchusDineIn(dlg1)
    bacchusDineInOTK(dlg1, dlg2)

    if checkIfExist(dlg1, 'Server?'):
        clickBckMgrMenu(dlg1, 'bacchusx')
    if checkIfExist(dlg2, 'Server?'):
        clickBckMgrMenu(dlg2, 'bacchusx')

    bacchusTakeOut(dlg1)
    bacchusTakeOutOTK(dlg1, dlg2)

    if checkIfExist(dlg1, 'Server?'):
        clickBckMgrMenu(dlg1, 'bacchusx')
    if checkIfExist(dlg2, 'Server?'):
        clickBckMgrMenu(dlg2, 'bacchusx')

    delivery(dlg1)
    
    if checkIfExist(dlg, 'Trans#', control_type="HeaderItem"):
        clickBckMgrMenu(dlg1, 'x')

    bulk(dlg1)
    

    

if __name__ == "__main__":
    main()
