from Ressources.Code.Archiver import Archiver
from Ressources.Code.Imports import *

bootos = str(platform.release())
if bootos == "10":
    print("OS: Windows 10")
elif bootos == "8.1":
    print("OS: Windows 8.1")
elif bootos == "8":
    print("OS: Windows 8")
elif bootos == "7":
    print("OS: Windows 7")
elif int(bootos) < 7:
    print("Panic!")

def space(a):
    for i in range(0, a):
        print("")
    i = 0


windows_release_integer = str(platform.release())
if windows_release_integer == "8.1":
    windows_release_integer == 8
else:
    windows_release_integer == int(windows_release_integer)
if windows_release_integer == 10:
    consolewide = 120
else:
    consolewide = 50




def toasteur(toaston, titre, description, ico, dure=10):
    if toaston == 0:
        toaster = ToastNotifier()
        toaster.show_toast(titre,
                           description,
                           icon_path=ico,
                           duration=dure)





#tempa = time.localtime()
#ny = int(time.strftime("%y", tempa)) + 2000
#nm = int(time.strftime("%m", tempa))
#nd = int(time.strftime("%d", tempa))
#nh = int(time.strftime("%H", tempa))
#nmi = int(time.strftime("%M", tempa))
#ns = int(time.strftime("%S", tempa))

debug = 0
pata = 0
space(2)

# startup end!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
while 1:
    # menu
    try:
        print("")
        print("1) Archiver")
        print("2) Restaurer archive ")
        print("3) Option")
        print("0) Quitter")
        print("")

        tempa = int(input(""))
    except ValueError:
        print("")

    if tempa == 0:
        break
    elif tempa == 115:
        debug = debug + 1
        if debug == 3:
            debug = "on"
            print("Debug on")
        elif debug == "on":
            debug = 0

    elif tempa == 1:
        Archiver("")
    ##end archivage!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    elif tempa == 2:
        ##restaur!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("loading archives...")
        print("")
        tempa = 0
        print("0) retour")
        for root, dirs, files in os.walk(archiveroot):
            while 1:
                rescount = 1
                if root == archiveroot:
                    for dire in dirs:
                        print(str(rescount) + ") " + str(dire))
                        rescount = rescount + 1
                    archivenum = int(input(""))
                    if archivenum == 0:
                        break
                    rescount = 1
                    for dire in dirs:
                        if rescount == archivenum:
                            archivenum = str(root) + str(dire) + "\\"
                            print(archivenum)
                            tempa = 1
                            break
                        rescount = rescount + 1
                if tempa == 1:
                    break
            if archivenum == 0:
                break
            else:
                while 1:
                    print("")
                    disque = str(input("Restaurer l'archive sur quel disque " + '(ex: "F:")')) + "\\"
                    if os.path.exists(disque):
                        break
                    else:
                        print("")
                        print("Le nom du disque est invalide")
                print("Restauration...")
                fil = 0
                if not "idlelib" in sys.modules:
                    for r, d, f in os.walk(archivenum):
                        for fi in f:
                            fil = fil + 1
                transfernum = 0
                permeror = False

                for root, directories, filenames in os.walk(archivenum):

                    for dire in directories:
                        if not os.path.exists(
                                str(disque) + str(root.replace(str(archivenum), '') + "\\" + str(dire) + "\\")):
                            newdirectory(str(disque) + str(root.replace(str(archivenum), '') + "\\" + str(dire) + "\\"))

                    for filename in filenames:
                        transfernum = transfernum + 1
                        if not filename == "info.txt":
                            try:
                                progress(transfernum, fil, consolewide, " Restauration")
                                shutil.move(str(root) + "\\" + str(filename),
                                            str(disque) + str(root.replace(str(archivenum), '') + "\\"))
                            except shutil.Error:
                                pass
                            except PermissionError:
                                permeror = True

                space(2)
                print("Done !")
                winsound.PlaySound(
                    "F:\\Program Files (x86)\\Python Programs\\Data\\Archivage\\Windows Proximity Notification.wav",
                    winsound.SND_FILENAME)
                if True == permeror:
                    toasteur(notoast, "Pas de permition", "Des fichier n'ont pas pus être restaurés",
                             "F:/Program Files (x86)/Python Programs/Data/Archivage/attention_PNG60.ico", 20)
                time.sleep(5)
                break

    elif tempa == 3:
        while 1:
            print("")
            print("1) Changer le dossier d'archive")
            print("2) Affichage")
            print("0) Retour ")
            print("")

            tempa = str(input(""))
            if tempa == "1":
                while 1:
                    print("Change le dossier ou les archives sont enregistrés")
                    print("Par default, elle sont sauvegarder dans \\Program Files (x86)\\Python Programs\\archivage\\")
                    print('Pour remetre a zero, tapez "reset"')
                    print("")
                    tempa = input("")
                    print("")
                    if tempa != "reset":
                        if os.path.exists(tempa):
                            with open("\\Program Files (x86)\\Python Programs\\Data\\Archivage\\archiveroot.txt",
                                      mode="w") as fichier:
                                if "\\" != tempa[-1:]:
                                    tempa = tempa + "\\"
                                print(tempa)
                                fichier.write(tempa)
                                archiveroot = tempa
                                break
                        else:
                            print("Le chemin n'existe pas")
                            print("")
                    else:
                        with open("\\Program Files (x86)\\Python Programs\\Data\\Archivage\\archiveroot.txt",
                                  mode="w") as fichier:
                            fichier.write("none")
                            break
            elif tempa == "2":
                print("1) Complet")
                print("2) Partiel")
                print("0) Retour")
                print("")
                tempa = str(input(""))
                if tempa == "1":
                    showmod = "all"
                elif tempa == "2":
                    showmod = "prog"
                elif tempa == "0":
                    break
            elif tempa == "0":
                break

    space(60)
