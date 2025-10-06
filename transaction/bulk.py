from function.clickButton import clickBtn
from function.util import checkIfExist
from procedure.punch_bulk import punch_bulk
from configuration.config import config

def bulk(dlg, trantype='BULK\r\nORDER'):
    sequence = config.bulk.punching_sequence
    if(len(sequence) > 0 and checkIfExist(dlg, trantype)):
        clickBtn(dlg, trantype)
    for punch_data in sequence:
        punch_bulk(dlg, **vars(punch_data))
    
    
