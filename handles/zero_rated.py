from function.clickButton import clickBtn
from function.clickZeroRated import clickZeroRated

def zero_rated(dlg):
    clickBtn(dlg, 'ZERO\r\nRATED')
    clickZeroRated(dlg)