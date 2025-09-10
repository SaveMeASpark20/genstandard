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
from function.clickButton import clickKeypad
from handles.tender_amount import tender_amount
from handles.cashier_sign_setup_table import cashier_sign_setup_table
from handles.open_reg import open_reg



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

    # try:
    #     # Mapping of index to keypad value (reversed from your original)
    #     IndexToKeypadVal = {
    #         0: "arrow_up",
    #         1: 7,
    #         2: 8,
    #         3: 9,
    #         4: "arrow_down",
    #         5: 4,
    #         6: 5,
    #         7: 6,
    #         8: "exact amount",
    #         9: 1,
    #         10: 2,
    #         11: 3,
    #         12: "x",
    #         13: 0,
    #         14: ".",
    #         15: "check"
    #     }

    #     for index in range(16):  # You only have 16 mapped buttons (0 to 15)
    #         try:
    #             button = dlg2.child_window(control_type="Button", found_index=index)

    #             value = IndexToKeypadVal.get(index, "Unknown")

    #             print(f"🖱️ Clicking button at index {index} → '{value}'")
    #             button.click_input()
    #         except Exception as inner_e:
    #             print(f"❌ Could not click button at index {index}: {inner_e}")

    # except Exception as e:
    #     print(f"❌ Outer exception: {e}")

    # # Step 2: Open main POS window if not found
    # if dlg1 is None:
    #     print("⚠️ POS window not found, launching...")
    #     dlg1 = openGo()
    #     managerSignon(dlg1)
    #     cashierSignon(dlg1)

    # clickBtn(dlg1, 'DINE IN')

    # # Step 3: Handle OTK (optional)
    # if dlg2 is None:
    #     print("ℹ️ OTK window not found, launching...")
    #     dlg2 = openGo(is_OTK=True)
    #     managerSignon(dlg2)

    # clickBtn(dlg2, 'DINE IN')

    # cashier_sign_setup_table(dlg2, 22, 'TABLE 1')

    dlg.print_control_identifiers()
    open_reg(dlg)
    # tender_amount(dlg1,amounts=None, tenders=['CASH'])

if __name__ == "__main__":
    main()



    
