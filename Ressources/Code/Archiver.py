from Ressources.Code.Imports import *
import time

class Archiver:
    def __init__(self):
        self.e = "e"

    def Get_expiration_date(self, mode="date"):
        if mode == "date":
            datej = int(input("Jour: "))
            datem = int(input("Mois: "))
            datea = int(input("Année: "))

            date_string = "{}/{}/{}".format(datej, datem, datea)
            print("")
            print("Limite set to: " + date_string)
            self.datelim = time.mktime(time.strptime(date_string, "%d/%m/%Y"))

    def Get_path(self):
        print("")
        path = str(input("\\Chemin\\Dossier : "))
        print("")

        if not path[-2: -1] == "\\": # is there \\ at the end ?
            path = str(path) + "\\"

        if os.path.exists(path): # does this folder exist ?
            self.path = path
        else:
            raise Exception("Ce dossier n'existe pas")

    def Archivage(self):
        tempa = time.gmtime(time.time())
        ny = int(time.strftime("%y", tempa)) + 2000
        nm = int(time.strftime("%m", tempa))
        nd = int(time.strftime("%d", tempa))
        nh = int(time.strftime("%H", tempa))
        nmi = int(time.strftime("%M", tempa))
        ns = int(time.strftime("%S", tempa))
        newarchive = "\\" + "Archives" + "\\" + "archive" + " " + str(nd) + "_" + str(nm) + "_" + str(ny) + "\\"

        self.Get_expiration_date()
        self.Get_path()

        filecopy = []
        filenoperm = []
        filecopyfail = []

        filecountercheck = 0
        filecounter = 0

        for root, directories, filenames in os.walk(self.path):
            for filename in filenames:
                filecountercheck = filecountercheck + 1
                #todo put loading bar

                tempb = root[1:2]
                if tempb == ":":
                    pathrootless = root[2:]

                datefile = os.path.getmtime(os.path.join(root, filename))

                # deplacer ?

                if datefile <= self.datelim:
                    print("Archiver", filename)

                    try:
                        OS_Tools.newdirectory(newarchive + pathrootless)
                    except:
                        pass

                    try:
                        shutil.move(os.path.join(root, filename), newarchive + pathrootless)
                        filecopy.extend("\n" + str(filename))
                        filecounter = filecounter + 1
                    except PermissionError:
                        ##print("[Error] Permition Denied")
                        noperm = noperm + 1
                        filenoperm.extend("\n" + str(filename))
                    except shutil.Error:
                        ##print("Already in ! ")
                        copyfail = copyfail + 1
                        filecopyfail.extend("\n" + str(filename))
                    except FileNotFoundError:
                        ## what ???
                        pass

        if not os.path.exists(newarchive + "info.txt"):
            with open(newarchive + "info.txt", mode="w") as fichier:
                fichier.write("Archive of the " + str(nd) + "_" + str(nm) + "_" + str(ny))
        with open(newarchive + "info.txt", mode="a") as fichier:
            fichier.write("\n \n \n                       " + str(nh) + ":" + str(nmi) + ":" + str(
                ns) + "\n \n \n   Fichiers sans permition: \n ")
            for ele in filenoperm:
                fichier.write(ele)
            fichier.write("\n \n   Fichiers déjà presents dans l'archive: \n")
            for ele in filecopyfail:
                fichier.write(ele)
            fichier.write("\n \n   Fichiers copiés dans l'archive: \n")
            for ele in filecopy:
                fichier.write(ele)

        print("Done !")

