from Ressources.Code.Imports import *
from Ressources.Code.Archiver import Archiver # Fonction Archiver

while 1:
    print("")
    Command_line_utils.Menu(["1) Archiver", "2) Restaurer archive ", "3) Option", "0) Quitter"])
    print("")

    Action = int(input(""))

    if Action == 0: # Quit
        break

    elif Action == 1: # Archiver
        test = Archiver()
        test.Archivage()

    elif Action == 2: # Restaurer
        pass

    elif Action == 3: # Options
        pass