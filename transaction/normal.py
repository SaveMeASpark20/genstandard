from function.clickButton import clickBtn
from procedure.punch_normal import punch_normal
from function.util import checkIfExist
from configuration.config import config


def miscellaneous(dlg, trantype='MISC'):
    sequence = config.misc.punching_sequence 
    if(len(sequence) > 0 and checkIfExist(dlg, trantype)):
        clickBtn(dlg, trantype)
    for punch_data in sequence:
        punch_normal(dlg, **vars(punch_data))

