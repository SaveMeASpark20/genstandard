from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText_Re

def inputServerAndTable(dlg, isinputTable=False):
    inputText_Re(dlg, '22')
    clickKeypad(dlg, 'check')
    if(isinputTable):
        clickBtn(dlg, 'TABLE 1')
        inputText_Re(dlg, '1')
        clickKeypad(dlg, 'check')
