from function.clickButton import clickBtn
from procedure.punch_free import punch_free
from function.util import checkIfExist
from configuration.config import config


def free(dlg, trantype='FREE'):
    sequence = config.free.punching_sequence 
    if(len(sequence) > 0 and checkIfExist(dlg, trantype)):
        clickBtn(dlg, trantype)
    for punch_data in sequence:
        punch_free(dlg, **vars(punch_data))

