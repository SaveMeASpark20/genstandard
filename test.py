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
