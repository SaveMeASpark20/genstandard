from function.clickButton import clickBtn
from function.clickCustInfo import clickCustInfo
def cust_info(dlg):
    clickBtn(dlg, 'CUSTOMER\r\nINFO')
    clickCustInfo(dlg)