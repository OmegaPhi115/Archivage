with open("/Program Files (x86)/Python Programs/Data/Archivage/archiveroot.txt", mode="r") as fichier:
    archiveroot = fichier.read()
    if archiveroot == "none":
        archiveroot = "\\Program Files (x86)\\Python Programs\\archivage\\"