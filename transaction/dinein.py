from function.clickButton import clickBtn
from procedure.punch import punch
from procedure.punch_OTK import punch_OTK
from function.util import checkIfExist
from configuration.config import config
from procedure.punch_normal import punch_normal


def bacchusDineIn(dlg, trantype='DINE IN'):
    sequence = config.bac_dine_in.punching_sequence
    if(len(sequence) > 0 and checkIfExist(dlg, trantype)):
        clickBtn(dlg, trantype)
    for punch_data in sequence:
        punch(dlg, **vars(punch_data))
    
    
def bacchusDineInOTK(dlg1, dlgOTK, trantype='DINE IN'):
    
    # clickBtn(dlgOTK, trantype)
    sequence = config.bac_dine_in_OTK.punching_sequence
    if (len(sequence) > 0 and checkIfExist(dlg1, trantype)):
        clickBtn(dlg1, trantype)
    if (len(sequence) > 0 and checkIfExist(dlgOTK, trantype)):
        clickBtn(dlgOTK, trantype)
    for punch_data in sequence:
        punch_OTK(dlg1, dlgOTK, **vars(punch_data))


def fd_dinein(dlg, ui_button='DINE IN'):
    sequence = config.food_dinein.punching_sequence
    if (len(sequence) > 0 and checkIfExist(dlg, ui_button)):
        clickBtn(dlg, ui_button)

    # punch data(each punch data object)
    # punch_data -> object
    # vars() -> turns object attributes into a dictionary
    # ** -> unpacks the dictionary into keyword arguments for the punch_normal function
    for punch_data in sequence:
        punch_normal(dlg, trantype='FOOD_DINEIN', **vars(punch_data))