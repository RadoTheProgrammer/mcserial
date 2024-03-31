import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
ESPACE=block.AIR.id
MUR=block.GOLD_BLOCK.id
SOL=block.GRASS.id
NOMDEFICHIER="labyrinthe1.csv"
f=open(NOMDEFICHIER,"r")
pos=mc.player.getTilePos()
ORIGINE_X=pos.x+1
ORIGINE_Y=pos.y
ORIGINE_Z=pos.z+1
z=ORIGINE_Z
for line in f.readlines():
    data=line.split(",")
    x=ORIGINE_X
    for cell in data:
        if cell=="0":
            b=ESPACE
        else:
            b=MUR
        mc.setBlock(x,ORIGINE_Y,z,b)
        mc.setBlock(x,ORIGINE_Y+1,z,b)
        mc.setBlock(x,ORIGINE_Y-1,z,SOL)
        x=x+1
    z=z+1
