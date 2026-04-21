from function.input import inputText_Re
from function.util import checkIfExist
from function.clickButton import clickBtn, clickKeypad


def handle_head_count(dlg, head_count=1, yes_button='YES'):

    has_head_count = checkIfExist(dlg, 'Head Count:', control_type='Text')

    if not has_head_count:
        return

    success = inputText_Re(dlg, head_count, 'Head Count')
    if not success:
        return

    clickKeypad(dlg, 'check')
    clickBtn(dlg, yes_button)
