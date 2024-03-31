import mcpi.minecraft as minecraft
import mcpi.block as block
import glob
import time
import random
mc=minecraft.Minecraft.create()
DIMENSIONSX=10
DIMENSIONSY=10
DIMENSIONSZ=10
sallex=None
salley=None
sallez=None
def constructionSalle(x,y,z):
    global sallex,salley,sallez
    sallex=x
    salley=y
    sallez=z
    mc.setBlocks(sallex,salley,sallez,sallex+DIMENSIONSX+2,salley+DIMENSIONSY+2,sallez+DIMENSIONSZ+2,block.GLASS.id)
    mc.setBlocks(sallex+1,salley+1,sallez,sallex+DIMENSIONSX+1,salley+DIMENSIONSY+1,sallez+DIMENSIONSZ+1,block.AIR.id)
def demolitionSalle():
    if sallex==None:
        print("Tu dois avoir une salle pour le faire.")
        break
    mc.setBlocks(sallex,salley,sallez,sallex+DIMENSIONSX+2,salley+DIMENSIONSY+2,sallez+DIMENSIONSZ+2,block.AIR.id)
def nettoyageSalle():
    if sallex==None:
        print("Tu dois avoir une salle pour le faire.")
        break
    mc.setBlocks(sallex+1,salley+1,sallez+1,sallex+DIMENSIONSX+1,salley+DIMENSIONSY+1,sallez+DIMENSIONSZ+1,block.AIR.id)
def repertoireFichiers():
    print("\nFICHIERS:")
    fichiers=glob.glob("*.csv")
    for nomdefichier in fichiers:
        print(nomdefichier)
    print("\n")
def scannage3D(nomdefichier,originex,originey,originez):
    if sallex==None:
        print("Tu dois avoir une salle pour le faire.")
        break
    f=open(nomdefichier,"w")
    f.write(str(DIMENSIONSX)+","+str(DIMENSIONSY)+","+str(DIMENSIONSZ)+"\n")
    for y in range(DIMENSIONSY):
        mc.postToChat("scannage en cours :"+str(y))
        f.write("\n")
        for x in range(DIMENSIONSZ):
            line=""
            for z in range(DIMENSIONSZ):
                blockid=mc.getBlock(originex+x,originey+y,originez+z)
                if line!="":
                    line=line+","
                line=line+str(blockid)
            f.write(line+"\n")
    f.close()
def impression3D(nomdefichier,originex,originey,originez):
    if sallex==None:
        print("Tu dois avoir une salle pour le faire.")
        break
    f=open(nomdefichier,"r")
    lignes=f.readlines()
    coords=lignes[0].split(",")
    dimensionsx=int(coords[0])
    dimensionsy=int(coords[1])
    dimensionsz=int(coords[2])
    idxligne=1
    for y in range(dimensionsy):
        mc.postToChat(str(y))
        idxligne=idxligne+1
        for x in range(dimensionsx):
            ligne=lignes[idxligne]
            idxligne=idxligne+1
            donnee=ligne.split(",")
            for z in range(dimensionsz):
                blockid=int(donnee[z])
                mc.setBlock(originex+x,originey+y,originez+z,blockid)
def menu():
    while True:
        print("MENU DU DUPLICATEUR")
        print("1. CONSTRUIRE la salle de reproduction")
        print("2. AFFICHER les fichiers existants")
        print("3. SCANNER le contenu de la salle de reproduction dans un fichier")
        print("4. CHARGER le contenu d'un fichier dans la salle de reproduction")
        print("5. IMPRIMER le contenu de la salle de reproduction en face de Steve")
        print("6. NETTOYER la salle de reproduction")
        print("7. DEMOLIR la salle de reproduction")
        print("8. FERMER")
        choix=input("choix : ")
        if type(choix)!=int:
            print("Ca doit être un nombre entier")
        else:
            choix=int(choix)
            if choix<1 or choix>8:
                print("Tu dois choisir un chiffre entre 1 et 8")
            else:
                return choix
anotherGo=True
while anotherGo:
    choix=menu()
    if choix==1:
        pos=mc.player.getTilePos()
        constructionSalle(pos.x,pos.y,pos.z)
    elif choix==2:
        repertoireFichiers()
    elif choix==3:
        nomdefichier=input("nom du fichier ?")
        scannage3D(nomdefichier,sallex+1,salley+1,sallez+1)
    elif choix==4:
        nomdefichier=input("nom du fichier ?")
        impression3D(nomdefichier,sallex+1,salley+1,sallez+1)
    elif choix==5:
        scannage3D("scantemp",sallex+1,salley+1,sallez+1)
        pos=mc.player.getTilePos()
        impression3D("scantemp",pos.x+1,pos.y,pos.z+1)
    elif choix==6:
        nettoyageSalle()
    elif choix==7:
        demolitionSalle()
    elif choix==8:
        anotherGo=False
        
                     
