from pywinauto import Application
# from pywinauto.findwindows import ElementNotFoundError
from sequence.managerSignon import managerSignon
from sequence.openGo import openGo
from configuration.config import config
from transaction.dinein import bacchusDineIn, bacchusDineInOTK
from transaction.takeout import bacchusTakeOut
from transaction.takeout import bacchusTakeOutOTK
from transaction.delivery import delivery
from transaction.bulk import bulk
from transaction.normal import miscellaneous
from transaction.dinein import fd_dinein
from transaction.normal import transaction
from transaction.free import free
from sequence.cashierSignon import cashierSignon
# from handles.tender_amount import tender_amount
from pywinauto.findwindows import find_elements
# from function.clickButton import clickBtn
from function.util import checkIfExistWithTitleRe
from handles.open_reg import open_reg
from sequence.backMgrMenu import clickBckMgrMenu
# from configuration.config import config
from transaction.open_auto import open_auto
from procedure.manager_procedure import m_void
import time

# backend="uia" default param.


def main(backend="uia"):

    otk_no = getattr(config, "OTK", False)
    pos_no = getattr(config, "POS", False)
        
    # pos_no = None
    # otk_no = None
    
    # if config.POS:
    #     pos_no = config.POS
    # if config.OTK:
    #     otk_no = config.OTK or None
    restaurant_type = config.restaurant_type
    dlg1, dlg2 = None, None

    # Step 1: Scan open windows / Find all matching windows.
    windows = find_elements(title_re=".*W I N V Q P.*", control_type="Window", backend=backend)

    for elem in windows:
        if dlg1 and dlg2:
            print("Dialog1"+str(dlg1)+"Dialog2"+str(dlg2))
            break
        app = Application(backend=backend).connect(handle=elem.handle)
        dlg = app.window(handle=elem.handle)

        # look ffor element with title = pos_no
        if dlg.child_window(title=pos_no, control_type="Text").exists():
            dlg1 = dlg
            print("✅ Identified App1 (POS)")

        elif dlg.child_window(title=otk_no, control_type="Text").exists():
            dlg2 = dlg
            print("✅ Identified App2 (OTK)")

    # Step 2: Open main POS window if not found
    if dlg1 is None and pos_no:
        print("⚠️ POS window not found, launching...")
        dlg1 = openGo()
        dlg1.set_focus()
        managerSignon(dlg1)
        cashierSignon(dlg1)

    if dlg2 is None and otk_no:
        print("ℹ️ OTK window not found, launching...")
        dlg2 = openGo(is_OTK=True)
        dlg2.set_focus()
        managerSignon(dlg2)
        open_reg(dlg2)
        cashierSignon(dlg2)

    run = config.run_standard

    def whatIsTransaction():
        for transaction in ["DINE IN", "TAKE OUT", "DELIVERY", "MISC", "FREE", "BULK ORDER"]:
            if(checkIfExistWithTitleRe(dlg1, transaction, 'HeaderItem')):
                return transaction
        return None
    
    for step in run:
        action = getattr(step, 'action', None) or getattr(step, '_action', None)
        if not action:
            print(f"Comment: {getattr(step, '_comment', 'No comment provided')}")
            continue

        
        if action and action.startswith('open'):
            print("1", action)
            open_auto(dlg1, action)
            
        elif action and action.startswith('manager_void'):
            print("2", action)
            m_void(dlg1, action)

        elif action == "BACCDI":
            print("3", action)
            bacchusDineIn(dlg1)
        
        elif action == "BACCDIOTK":
            print("4", action)
            bacchusDineInOTK(dlg1, dlg2)
        
        elif action == "BACCTO":
            print("5", action)
            bacchusTakeOut(dlg1)
        
        elif action == "BACCTOOTK":
            print("6", action)
            bacchusTakeOutOTK(dlg1, dlg2)

        elif action == "DELIVERY":
            print("7", action)
            delivery(dlg1)
            
        elif action == "BULK":
            print("8", action)
            bulk(dlg1)

        elif action == 'MISC':
            print("9", action)
            miscellaneous(dlg1)

        elif action == 'CASHIER_SIGN':
            print("10", action)
            
            cashierSignon(dlg1)
        
        elif(action == 'FREE'):
            print("11", action)
            free(dlg1)

        elif action == 'BACKTOMGR':
            print("12", action)
            currentTransaction = whatIsTransaction()

            if (currentTransaction == None):
                print("Can't find Transaction")
                continue
            if currentTransaction == "DELIVERY":
                backToMgr = "x"
            elif restaurant_type == "FINE DINING" and currentTransaction in ["TAKE OUT", "DINE IN"]:
                backToMgr = "bacchusx"
                print("restaurant_type :", restaurant_type)
                print("Current_Transaction :", currentTransaction )
            else:
                backToMgr = "MGR MENU"
            print(backToMgr)
            clickBckMgrMenu(dlg1, backToMgr)
        elif action == 'DINE IN':
            transaction(dlg1, action)
        elif action == 'FOOD_DINEIN':
            # POS1 only, no need to check transaction type
            print("11", action, dlg1)
            fd_dinein(dlg1)

        else:
            print("cant find the action: ", action)


if __name__ == "__main__":
    main()
