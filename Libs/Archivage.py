import tkinter as tk
import Directory_Browser as Dir_ask

"""Class responsable de l'archivage"""

class inputs():
    """je recuperre les entrées !"""
    def Dossier(self):
        return Dir_ask.run()

    def __init__(self):
        input_fen = tk.Tk()
        mode = ""
        path = self.Dossier()




class found_file():
    """je cherche les fichier et je les tri"""
    pass

class archive():
    """je met les fichiers dans une archive"""


def execute_archivage(self):
    """Veut faire un archivage ? execute moi !"""
    pass

inputs()

def old_archi():
    noperm = 0
    filecounter = 0
    copyfail = 0
    dino = 0
    filecopy = []
    filenoperm = []
    filecopyfail = []
    filecountercheck = 0
    newarchive = str(archiveroot) + "archive" +" "+ str(nd) + "_" + str(nm) + "_" + str(ny) + "\\"
    while 1:
        print("input type:")
        print("1) date")
        if nodateutil == 0:
          print("2) durée")
        print("0) retour")

        try:
                intype = int(input(""))
                if intype == 1:
                          break
                elif intype == 2:
                    if nodateutil == 0 :
                          break
                elif intype == 0:
                          break

        except ValueError:
                print("veullier entrer un chiffre")

    if intype != 0:
        if 1 :
            while 1:
                    try:
                              print("")
                              datej = int(input("Jour: "))
                              datem = int(input("Mois: "))
                              datea = int(input("Année: "))
                              if intype == 1:
                                        if datea <= 1970:
                                                  dino = dino + 1
                                                  if dino == 5:
                                                            os.startfile('\\Program Files (x86)\\Python Programs\\Data\\Archivage\\téléchargement.png')
                                                  raise AssertionError("")
                                        s = str(datej) + "/" + str(datem) + "/" + str(datea)
                                        print("")
                                        print("Limite set to: " + s)
                                        datelim = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
                                        break
                              else:
                                        #input tipe 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                        today = date.today()
                                        today = str(today + relativedelta(years = -datea, months = -datem, days = -datej)).replace("-","/")
                                        print("")
                                        print(today)
                                        try:
                                                  datelim = time.mktime(datetime.datetime.strptime(today, "%Y/%m/%d").timetuple())
                                                  break
                                        except OverflowError:
                                                  print("")
                                                  print("Les ordinateurs n'existait pas encore, Veuiller entrer une date supérieure a l'epoch (1970)")
                                                  print("")
                    except ValueError:
                              print("")
                              print("Ce n'est pas une date")
                              print("")
                    except AssertionError:
                              print("")
                              print("Les ordinateurs n'existait pas encore, Veuiller entrer une date supérieure a l'epoch (1970)")
                              print("")

            #file transfer
            while 1:
                    print("")
                    path =  str(input("\\Chemin\\Dossier : "))
                    print("")

                    tempa = path[:1]
                    tempb = path[1:3]
                    if not tempa == "\\":
                              if not tempb == ":\\":
                                        path = "\\" + path

                    tempb = path[-2: -1]
                    if not tempb == "\\":
                              path = str(path) +"\\"
                    if not os.path.exists(path):
                              print("Ce dossier n'existe pas")
                    else:
                              break
            print("Loading...")
            print("")

            toasteur(notoast, "Archivage commencé", "Archivage des donnés de " + str(path), "/Program Files (x86)/Python Programs/Data/Archivage/454.ico", 10)

            #os walk

            if not "idlelib" in sys.modules:
                    fil = 0
                    for root, directories, filenames in os.walk(path):
                            for file in filenames:
                                    fil = fil + 1
            else:
                    fil = 0

            for root, directories, filenames in os.walk(path):
               for filename in filenames:
                    filecountercheck = filecountercheck + 1
                    progress(filecountercheck, fil, consolewide, str(" Archivage"))
                          ##print("Loading: " + os.path.join(root,filename))

                    tempb = root[1:2]
                    if tempb == ":":
                              pathrootless = root[2: ]

                    datefile = os.path.getmtime(os.path.join(root,filename))

                    #deplacer ?

                    if datefile <= datelim :
                                       ## print("Archiver", filename)

                              newdirectory(newarchive + pathrootless)

                              try:
                                        shutil.move(os.path.join(root, filename), newarchive + pathrootless)
                                        secondout("Archiver " + filename, secondouton)
                                        filecopy.extend( "\n" + str(filename))
                                        filecounter = filecounter + 1
                              except PermissionError:
                                ##print("[Error] Permition Denied")
                                        noperm = noperm + 1
                                        filenoperm.extend( "\n" + str(filename))
                              except shutil.Error:
                                 ##print("Already in ! ")
                                        copyfail = copyfail + 1
                                        filecopyfail.extend( "\n" + str(filename))
                              except FileNotFoundError:
                                        ## what ???
                                        pass

            if not os.path.exists(newarchive + "info.txt"):
                    with open(newarchive + "info.txt", mode="w") as fichier:
                              fichier.write("Archive of the " + str(nd) + "_" + str(nm) + "_" + str(ny))

            with open(newarchive + "info.txt", mode = "a") as fichier:
                    fichier.write("\n \n \n                       " + str(nh) + ":" + str(nmi) + ":" + str(ns) + "\n \n \n   Fichiers sans permition: \n ")
                    for ele in filenoperm:
                        fichier.write(ele)
                    fichier.write("\n \n   Fichiers déjà presents dans l'archive: \n")
                    for ele in filecopyfail:
                        fichier.write(ele)
                    fichier.write("\n \n   Fichiers copiés dans l'archive: \n")
                    for ele in filecopy:
                        fichier.write(ele)

            #toasteur(notoast, "Archivage commencé", "Archivage des donnés , "ico", dure)

            toasteur(notoast, "Archivage terminé", "Sur " + str(filecountercheck) + " fichiers, " + str(filecounter) + " ont été déplacés", "/Program Files (x86)/Python Programs/Data/Archivage/transparent-green-checkmark-hi.ico", 5)

            if notoast == 0:
                if noperm != 0 :
                        toaster = ToastNotifier()
                        toaster.show_toast("Pas de Permition",
                                           str(noperm) + " fichiers n'ont pas put êtres deplacés. Plus d'informations sont disponible dans le fichier Info.txt de l'archive",
                                           icon_path="/Program Files (x86)/Python Programs/Data/Archivage/attention_PNG60.ico",
                                           duration=20)

                if noperm == 0:
                        if copyfail == 0:
                                  toaster = ToastNotifier()
                                  toaster.show_toast("Tout les fichiers ont bien été déplacés"," ",icon_path="/Program Files (x86)/Python Programs/Data/Archivage/transparent-green-checkmark-hi.ico", duration=5)

                if copyfail != 0:
                        toaster = ToastNotifier()
                        toaster.show_toast("Probleme de copie",
                                           str(copyfail) + " fichiers n'ont pas put êtres deplacés. Les fichiers sont deja dans l'archive, il doivent être deplacés manuellement. Plus d'informations sont disponible dans le fichier Info.txt de l'archive",
                                           icon_path="/Program Files (x86)/Python Programs/Data/Archivage/attention_PNG60.ico",
                                           duration=20)

            space(2)
            print("Done !")
            winsound.PlaySound("F:\\Program Files (x86)\\Python Programs\\Data\\Archivage\\Windows Proximity Notification.wav", winsound.SND_FILENAME)
            time.sleep(5)
