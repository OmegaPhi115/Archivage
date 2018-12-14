##startup!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##inport??????????????????????????????????????????????????????????????????????????????
#import sans problemes
import os, time, datetime, shutil, calendar, sys
import winsound
#import avec problemes
import platform
while 1:
    try:
        from win10toast import ToastNotifier
        notoast = 0
        break
    except:
        notoast = 1
        print("win10toast Notifier not found !")
        break

try:
          from datetime import *; from dateutil.relativedelta import *
          nodateutil = 0
except:
          nodateutil = 1
          print("Dateutil not found")



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


with open("/Program Files (x86)/Python Programs/Data/Common/shellheight - on.txt", mode = "r") as fichier:
          shellheight = str(fichier.read())
          if shellheight == "1":
                            with open("/Program Files (x86)/Python Programs/Data/Common/shellheight.txt", mode = "r") as fichier:
                                      shellheight = fichier.read()

with open("/Program Files (x86)/Python Programs/Data/Archivage/archiveroot.txt", mode = "r") as fichier:
          archiveroot = fichier.read()
          if archiveroot == "none":
                    archiveroot = "\\Program Files (x86)\\Python Programs\\archivage\\"

def space (a) :
    for i in range (0,a):
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
def progress(count, total, bar_len, status=''):
    if not "idlelib" in sys.modules:
              filled_len = int(round(bar_len * count / float(total)))

              percents = round(100.0 * count / float(total), 1)
              bar = '=' * filled_len + '-' * (bar_len - filled_len)

              sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
              sys.stdout.flush()

def test(a):
          print("test " + str(a))

secondouton = 0
def secondout(io, secondouton):
          if secondouton == 1:
                    with open("/Program Files (x86)/Python Programs/Data/2output/Nouveau document texte.txt", mode="w") as fichier:
                              fichier.write(io)

def toasteur (toaston, titre, description, ico, dure = 10):
          if toaston == 0:
                    toaster = ToastNotifier()
                    toaster.show_toast(titre,
                             description,
                             icon_path=ico,
                             duration = dure)

def newdirectory (newdoss):
          if not os.path.exists(newdoss):
                    try:
                               os.makedirs(newdoss)
                    except OSError :
                              pass


tempa = time.localtime()
ny = int(time.strftime("%y", tempa))+ 2000
nm = int(time.strftime("%m", tempa))
nd = int(time.strftime("%d", tempa))
nh = int(time.strftime("%H", tempa))
nmi = int(time.strftime("%M", tempa))
ns = int(time.strftime("%S", tempa))

debug = 0
pata = 0
space(100)

#startup end!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
while 1:
    #menu
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
            #Archivage
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
                                          for dire in dirs :
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
                                                    if not os.path.exists(str(disque) + str(root.replace(str(archivenum), '') + "\\" + str(dire) + "\\")):
                                                              newdirectory(str(disque) + str(root.replace(str(archivenum), '') + "\\" + str(dire) + "\\"))

                                          for filename in filenames:
                                                    transfernum = transfernum + 1
                                                    if not filename == "info.txt":
                                                              try:
                                                                        progress(transfernum, fil, consolewide, " Restauration")
                                                                        shutil.move(str(root) + "\\" + str(filename) , str(disque) + str(root.replace(str(archivenum), '') + "\\"))
                                                              except shutil.Error:
                                                                        pass
                                                              except PermissionError:
                                                                        permeror = True


                                space(2)
                                print("Done !")
                                winsound.PlaySound("F:\\Program Files (x86)\\Python Programs\\Data\\Archivage\\Windows Proximity Notification.wav", winsound.SND_FILENAME)
                                if True == permeror:
                                          toasteur (notoast, "Pas de permition", "Des fichier n'ont pas pus être restaurés", "F:/Program Files (x86)/Python Programs/Data/Archivage/attention_PNG60.ico", 20)
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
                                                              with open("\\Program Files (x86)\\Python Programs\\Data\\Archivage\\archiveroot.txt", mode = "w") as fichier:
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
                                                    with open("\\Program Files (x86)\\Python Programs\\Data\\Archivage\\archiveroot.txt", mode = "w") as fichier:
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
