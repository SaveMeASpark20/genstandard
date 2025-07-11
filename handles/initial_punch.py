from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickButton import clickNonBtn
from function.input import inputText
from pywinauto.keyboard import send_keys

def initial_punch(dlg, prod, counts, prod_parent,  prod_addons, qty_prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito, open_memo, open_memo_prod ):

    for index, (product, qty, parent,add_on, qpa, mc, qmc, si, psi, qsi, dt) in enumerate(zip(prod, counts, prod_parent, prod_addons, qty_prod_addons,  meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito )):
        current_parent =  prod_parent[0]
        if qty and product and parent:
                if dt == 1:
                    clickBtn(dlg, 'DI/TO')
                    clickBtn(dlg, 'OK')

                if parent == current_parent:
                    if(index == 0):
                        clickBtn(dlg, parent)
                    
                else :
                    clickBtn(dlg, 'RETURN')
                    clickBtn(dlg, parent)
                    current_parent = parent

                for _ in range(qty):
                    clickBtn(dlg, product)
                    if qmc and mc:
                        if not isinstance(mc, list):
                            mc = [mc]
                        
                        if not isinstance(qmc, list):
                            qmc = [qmc]


                        for meal_comp, qty in zip(mc, qmc):
                            for _ in range(qty):
                                clickBtn(dlg, meal_comp)
                            
                    if add_on and qpa :
                        if not isinstance(add_on, list):
                            add_on = [add_on]
                        
                        if not isinstance(qpa, list):
                            qpa = [qpa]

                        for qty, add in zip(qpa, add_on) :
                            for _ in range(qty) :
                                if add == 'CHECK' or add == 'SKIP':
                                    clickKeypad(dlg, "check")
                                else: 
                                    clickBtn(dlg, add)

                    if psi and si:
                        # clean_item = psi.replace("\r\n", " ")
                        # clickNonBtn(dlg, clean_item, control_type='Text')
                        clickBtn(dlg, "SPCL\r\nINSTRUCTN")
                        for _ in range(qsi):
                            clickBtn(dlg, si)
                    
                        clickKeypad(dlg, "check")

    if open_memo and open_memo_prod:
        for memo, prod in zip(open_memo ,open_memo_prod):
            clickNonBtn(dlg, prod, control_type='Text')
            clickBtn(dlg, 'OPEN MEMO')
            inputText(dlg, memo, 'Spcl Inst')
            send_keys("{ENTER}")


            
                
        

                
