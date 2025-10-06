from function.clickButton import clickBtn
from function.util import checkIfExist
from procedure.punch_delivery import punch_delivery
from configuration.config import config

def delivery(dlg, trantype='DELIVERY'):

    sequence = config.delivery.punching_sequence
    if(len(sequence) > 0 and checkIfExist(dlg, trantype)):
        clickBtn(dlg, trantype)
    for punch_data in sequence:
        punch_delivery(dlg, **vars(punch_data))
    
    
