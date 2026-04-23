from configuration.config import config
from function.util import checkIfExist
from function.clickButton import clickBtn
from function.input import inputText
from function.clickButton import clickBtnCoords
import re


def openautomate(dlg: any, action : str, **kwargs):
    print("running action :", action)
    for key, value  in kwargs.items():
        name = re.sub(r'\d+$', '', key)
        # number = int(re.search(r'\d+$', key).group())

        if(name == 'click'):
            clickBtn(dlg, value)
        
        elif(name == 'input'):
            print(value)
            inputText(dlg, text = value[0], name = value[1])

        elif(name == 'clickCoords'):
            clickBtnCoords(dlg, value) 
        
        else:
            print(name, "is not include on open automation")



    
