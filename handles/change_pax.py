from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText_Re
def change_pax(dlg, change_pax):
    clickBtn(dlg, 'TABLE\r\nFUNCTION')
    clickBtn(dlg, 'PAX')
    inputText_Re(dlg, change_pax, "PAX")
    clickKeypad(dlg, 'check')