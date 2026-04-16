from function.input import inputText_Re
from function.util import checkIfExist
from function.clickButton import clickBtn, clickKeypad
from handles.re_route import re_route
import time


def handle_head_count(dlg, head_count=1, yes_button='YES'):
    """Handle the POS head count prompt after exact amount payment."""
    has_head_count = (
        checkIfExist(dlg, 'Head Count', control_type='Text') or
        checkIfExist(dlg, 'Head Count:', control_type='Text') or
        checkIfExist(dlg, 'Head Count', control_type='Window')
    )

    if not has_head_count:
        return

    print(f"⚙️ Head Count prompt detected. Entering head count {head_count}.")
    success = inputText_Re(dlg, head_count, 'Head Count')
    if not success:
        print("⚠️ Failed to enter head count.")
        return

    time.sleep(0.5)

    if checkIfExist(dlg, 'check', control_type='Button') or checkIfExist(dlg, 'check', control_type='Text'):
        clickBtn(dlg, 'check')
    else:
        print("⚙️ 'check' button not detected as normal button, using keypad mapping.")
        clickKeypad(dlg, 'check')

    time.sleep(2)

    
    if checkIfExist(dlg, yes_button, control_type='Button'):
        clickBtn(dlg, yes_button)
        time.sleep(2)
    else:
        print(f"⚠️ '{yes_button}' button not found after head count input.")

    re_route(dlg)
