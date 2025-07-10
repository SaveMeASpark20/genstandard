from pywinauto import Application
import time
from configuration.config import config
from pywinauto.keyboard import send_keys
from function.clickButton import clickDeliveryBtn
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from function.input import inputTextByIndex
from function.util import checkIfExist
from function.util import checkIfExistWithRegex
from sequence.transanctions import delivery
from configuration.config import config
from sequence.openGo import openGo
"""Connects to the FASTFOOD application and clicks a button."""
restaurant_type = config.restaurant_type
# listToRun = config.run_main
app = Application(backend='uia').connect(title_re=".*" + restaurant_type + ".*")
dlg = app.window(title_re=".*" + restaurant_type + ".*")
# dlg.print_control_identifiers()

inputText(dlg, 3, "PAX")



if paxMoveTo and mark_prods and moveTo:
            clickBtn(dlg, 'TABLE\r\nFUNCTION')
            for mark_prod in mark_prods :
                clickNonBtn(dlg, mark_prod, control_type='TEXT')
                clickBtn(dlg, 'MARK')

            clickBtn(dlg, 'MOVE TO')
            clickBtn(dlg, moveTo)
            inputText(dlg, paxMoveTo, "PAX")
            send_keys("{ENTER}")
            clickBtn(dlg, 'OK')
            #clickKeypad(dlg, 'check')
            # clickBtn(dlg, 'FINAL\r\nPAYMENT')
            # clickBtn(dlg, 'CASH')
            # clickKeypad(dlg, 'exact amount')
            # clickBtn(dlg, 'OK')
            # inputText(dlg, cashier.cashier_id, "Server")
            # send_keys("{ENTER}")
            # clickBtn(dlg, moveTo)
            # clickKeypad(dlg, 'check')
            # clickBtn(dlg, 'FINAL\r\nPAYMENT')
            # clickBtn(dlg, 'CASH')
            # clickKeypad(dlg, 'exact amount')
