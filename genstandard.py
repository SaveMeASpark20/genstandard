import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from sequence.managerSignon import managerSignon
from sequence.openGo import openGo
from configuration.config import config
from transaction.dinein import bacchusDineIn
from sequence.cashierSignon import cashierSignon



def main(backend="uia"):
    """Connects to the FAST FOOD/FINE DINING application and clicks a button."""
    app=None
    dlg=None
    try:
        app = Application(backend=backend).connect(title_re=".*" +  "W I N V Q P" + ".*")
        dlg = app.window(title_re=".*" + "W I N V Q P" + ".*")
    except ElementNotFoundError:
        dlg = openGo()
        managerSignon(dlg)

    # cashierSignon(dlg)
    bacchusDineIn(dlg)
    


if __name__ == "__main__":
    main()
