import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
NOMDEFICHIER="arbre.csv"
DIMENSIONSX=5
DIMENSIONSY=5
DIMENSIONSZ=5
def scannage3D(nomdefichier,originex,originey,originez):
    f=open(nomdefichier,"w")
    f.write(str(DIMENSIONSX)+","+str(DIMENSIONSY)+","+str(DIMENSIONSZ)+"\n")
    for y in range(DIMENSIONSY):
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
pos=mc.player.getTilePos()
scannage3D(NOMDEFICHIER,pos.x-(DIMENSIONSX/2),pos.y,pos.z-(DIMENSIONSZ/2))
