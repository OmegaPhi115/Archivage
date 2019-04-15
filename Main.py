from Ressources.Code.Archiver import Archiver # Fonction Archiver


while 1:
    print("")
    print("1) Archiver")
    print("2) Restaurer archive ")
    print("3) Option")
    print("0) Quitter")
    print("")

    Action = int(input(""))

    if Action == 0: # Quit
        break

    elif Action == 1: # Archiver
        Archiver()

    elif Action == 2: # Restaurer
        pass

    elif Action == 3: # Options
        pass