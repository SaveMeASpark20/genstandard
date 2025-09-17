from function.clickButton import clickBtn
from function.util import checkIfExist
from procedure.punch_takeout import punch_takeout
from procedure.punch_takeout_OTK import punch_takeout_OTK

from configuration.config import config

def bacchusTakeOut(dlg, trantype='TAKE OUT'):

    sequence = config.take_out.punching_sequence
    if(len(sequence) > 0):
        clickBtn(dlg, trantype)
    for punch_data in sequence:
        punch_takeout(dlg, **vars(punch_data))
    
    
def bacchusTakeOutOTK(dlg2, dlgOTK, trantype='TAKE OUT'):
    
    # clickBtn(dlgOTK, trantype)
    sequence = config.take_out_OTK.punching_sequence
    if(len(sequence) > 0 and checkIfExist(dlg2, trantype)):
        clickBtn(dlg2, trantype)
    for punch_data in sequence:
        punch_takeout_OTK(dlg2, dlgOTK, **vars(punch_data))