from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText

def inputServerAndTable(dlg, isinputTable=False):
    inputText(dlg, '22')
    clickKeypad(dlg, 'check')
    if(isinputTable):
        clickBtn(dlg, 'TABLE 1')
        inputText(dlg, '1')
        clickKeypad(dlg, 'check')
