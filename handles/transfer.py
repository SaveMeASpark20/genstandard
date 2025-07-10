from function.clickButton import clickNonBtn
from function.clickButton import clickBtn

def transfer(dlg, transfers, control_type):
    for transfer in transfers:
        clickNonBtn(dlg, transfer, control_type=control_type)
        clickBtn(dlg, 'TRANSFER')