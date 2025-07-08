from function.clickButton import clickBtn
from procedure.punch import punch
from configuration.config import config

def bacchusDineIn(dlg, trantype='DINE IN'):
    clickBtn(dlg, trantype)
    sequence = config.dine_in.punching_sequence
    for punch_data in sequence:
        punch(dlg, **vars(punch_data))
        