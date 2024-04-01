from minecraftstuff import ShapeBlock,MinecraftShape
from mcpi.minecraft import Vec3,Minecraft
from time import sleep
class MinecraftSerial:
    def __init__(self,mc:Minecraft):
        self.mc=mc
    
    def Hit(self,txt):
        """The player hit a block and get the position of the block hit"""
        self.mc.postToChat(txt)
        self.mc.events.pollBlockHits()
        for event in self.mc.events.pollBlockHits():

            pos=event.pos
            b=self.mc.getBlockWithData(pos)
            self.mc.setBlock(pos,41)
            sleep(0.2)
            self.mc.setBlock(pos,b)
        
        return pos
    def scannage3D(self,origine,dimensions,show_charging=False):
        sc=show_charging
        if sc:
            print("="*100)
        data=str(dimensions.x)+","+str(dimensions.y)+","+str(dimensions.z)+"\n"
        a_scanner=dimensions.x*dimensions.y*dimensions.z
        deja_scanne=0
        dernier_scan=0
        for y in range(dimensions.y):
            data+="\n"
            for x in range(dimensions.x):
                line=""
                for z in range(dimensions.z):
                    blockid=self.mc.getBlockWithData(origine.x+x,origine.y+y,origine.z+z)
                    if line!="":
                        line=line+","
                    if blockid.data==0:
                        line=line+str(blockid.id)
                    else:
                        line=line+str(blockid.id)+"/"+str(blockid.data)
                    if sc:
                        deja_scanne+=1
                        scan=int((deja_scanne/a_scanner)*100)
                        if scan>dernier_scan:
                            print("|"*(scan-dernier_scan),end="")
                            dernier_scan=scan
                            
                        
                data+=line+"\n"
        #print(data)
        return data
    def impression3D(self,data,origine,show_charging=False):
        MinecraftShape(self.mc,origine,Data(data).ShapeBlocks())
def Calculer(coords1,coords2,ReturnOrigines=True,ReturnDimensions=True):
    if ReturnOrigines:
        origine=Vec3(
            min(coords1.x,coords2.x),
            min(coords1.y,coords2.y),
            min(coords1.z,coords2.z)
        )

    if ReturnDimensions:
        dimensions=Vec3(
            abs(coords1.x-coords2.x)+1,
            abs(coords1.y-coords2.y)+1,
            abs(coords1.z-coords2.z)+1
        )

    if ReturnOrigines:
        if ReturnDimensions:
            return origine,dimensions
        else:
            return origine
    else:
        if ReturnDimensions:
            return dimensions
def __replace(txtFormat):
    global _data
    _data=0
    _data=_data.replace(txtFormat.format(_old),txtFormat.format(_new))
class Data:
    def __init__(self,data):
        self.data=data
    def ShapeBlocks(self):
        lignes=self.data.splitlines()
        coords=lignes[0].split(",")
        dimensionsx=int(coords[0])
        dimensionsy=int(coords[1])
        dimensionsz=int(coords[2])
        Shapeblocks=[]
        for repeat in range(1):
            idxligne=1
            for y in range(dimensionsy):
                idxligne=idxligne+1
                for x in range(dimensionsx):
                    ligne=lignes[idxligne]
                    idxligne=idxligne+1
                    donnee=ligne.split(",")
                    for z in range(dimensionsz):
                        blockid=donnee[z].split("/")
                        if len(blockid)==1:
                            blockdata=0
                            
                        else:
                            blockdata=int(blockid[1])
                        Shapeblocks.append(ShapeBlock(x,y,z,int(blockid[0]),blockdata))
        return Shapeblocks
    def replace(old,new):
        global _data,_old,_new
        _data,_old,_new=self.data,old,new
        __replace("\n{}\n")
        __replace("\n{},")
        __replace(",{}\n")
        __replace(",{},")
        return Data(_data)

