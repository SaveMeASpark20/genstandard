from function.clickButton import clickBtn
from procedure.punch import punch
from procedure.punch_OTK import punch_OTK
from configuration.config import config

def bacchusDineIn(dlg, trantype='DINE IN'):
    sequence = config.dine_in.punching_sequence
    if(len(sequence) > 0):
        clickBtn(dlg, trantype)
    print(sequence)
    for punch_data in sequence:
        punch(dlg, **vars(punch_data))
    
    
def bacchusDineInOTK(dlg2, dlgOTK, trantype='DINE IN'):
    
    # clickBtn(dlgOTK, trantype)
    sequence = config.dine_in_OTK.punching_sequence
    if(len(sequence) > 0):
        clickBtn(dlg2, trantype)
    for punch_data in sequence:
        punch_OTK(dlg2, dlgOTK, **vars(punch_data))