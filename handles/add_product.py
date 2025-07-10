from function.clickButton import clickBtn
from function.clickButton import clickKeypad

def add_product(dlg, additional_prod_parent, additional_prod, additional_count, additional_addons): 
    additional_current_parent = additional_prod_parent[0]
    if additional_addons is None:
        additional_addons = [None] * len(additional_prod)

    for index,(product, qty, parent, add_on) in enumerate(zip(additional_prod, additional_count, additional_prod_parent, additional_addons)):
        if qty and product and parent:
            if parent == additional_current_parent:
                if(index == 0):
                    clickBtn(dlg, parent)
            else :
                clickBtn(dlg, 'RETURN')
                clickBtn(dlg, parent)
                additional_current_parent = parent

            for _ in range(qty):
                clickBtn(dlg, product)
                if add_on and (add_on == 'CHECK' or add_on == 'SKIP'):
                    clickKeypad(dlg, "check")
                elif add_on:    
                    clickBtn(dlg, add_on)