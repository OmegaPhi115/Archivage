import platform
import os, time, datetime, shutil, calendar, sys
import winsound
from Ressources.Code.Constantes import *

from Py_utils.Codes.OS_Tools.OS_Tools import *
from Py_utils.Codes.Command_line_utils.Command_line_utils import *

try:
    from win10toast import ToastNotifier
    notoast = 0
except:
    notoast = 1
    print("win10toast Notifier not found !")

try:
    from datetime import *
    from dateutil.relativedelta import *

    nodateutil = 0
except:
    nodateutil = 1
    print("Dateutil not found")