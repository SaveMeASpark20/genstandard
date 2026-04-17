from function.input import inputText_Re
from function.util import checkIfExist
from function.clickButton import clickBtn, clickKeypad
from handles.re_route import re_route
import time


def handle_head_count(dlg, head_count=1, yes_button='YES'):
    
    has_head_count = checkIfExist(dlg, 'Head Count:', control_type='Text')

    if not has_head_count:
        return

    success = inputText_Re(dlg, head_count, 'Head Count')
    if not success:
        return

    time.sleep(0.5)

    if checkIfExist(dlg, 'check', control_type='Button'):
        clickBtn(dlg, 'check')
    else:
        clickKeypad(dlg, 'check')

    if checkIfExist(dlg, yes_button, control_type='Button'):
        clickBtn(dlg, yes_button)
    else:
        print(f"⚠️ '{yes_button}' button not found after head count input.")

    re_route(dlg)