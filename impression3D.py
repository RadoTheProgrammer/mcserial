import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
NOMDEFICHIER="arbre.csv"
def impression3D(nomdefichier,originex,originey,originez):
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
pos=mc.player.getTilePos()
impression3D(NOMDEFICHIER,pos.x+1,pos.y,pos.z+1)
    
    
           
