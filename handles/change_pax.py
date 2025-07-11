from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
def change_pax(dlg, change_pax):
    clickBtn(dlg, 'TABLE\r\nFUNCTION')
    clickBtn(dlg, 'PAX')
    inputText(dlg, change_pax, "PAX")
    clickKeypad(dlg, 'check')