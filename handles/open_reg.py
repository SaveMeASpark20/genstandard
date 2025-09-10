from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.util import checkIfExist

def open_reg(dlg, open_reg = 'OPEN REG'):
    clickBtn(dlg, open_reg)
    if checkIfExist(dlg, "VQP", control_type='Window'):
        clickBtn(dlg, 'OK')
    if checkIfExist(dlg, "OPEN", control_type='Window'):
        clickBtn(dlg, 'OK')