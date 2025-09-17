from sequence.managerSignon import managerSignon
from function.clickButton import clickBtnInput
from function.clickButton import clickBtn

import time
def cancel_all(dlg, btn_name='CANCEL\r\nORDER'):
    time.sleep(2)
    clickBtnInput(dlg, btn_name)
    managerSignon(dlg)
    clickBtn(dlg, 'YES')