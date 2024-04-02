#from minecraftstuff import ShapeBlock,MinecraftShape

import time

from mcpi.minecraft import Vec3,Minecraft
from time import sleep
import numpy as np
from tqdm import tqdm
class MinecraftSerial:
    def __init__(self,mc:Minecraft):
        self.mc=mc
    

    def copy(self,coords1=None,coords2=None,use_tqdm=False):
        t.reset()
        coords,dims = self._copy_util(coords1,coords2)

        data=np.zeros((dims.y,dims.z,dims.x),dtype=np.float16)
        t.print("setup")

        #data=str(dims.x)+","+str(dims.y)+","+str(dims.z)+"\n"

        for y in tqdm(range(dims.y)) if use_tqdm else range(dims.y):
            for z in range(dims.z):
                for x in range(dims.x):
                    block=self.mc.getBlockWithData(coords.x+x,coords.y+y,coords.z+z)
                    if block.id==31:
                        pass
                    data[y,z,x]=block.id+block.data/100                      
                        
        #print(data)
        return data
    
    def _copy_util(self,coords1,coords2):
        coords1 = self._to_vec3(coords1,"Coords1")
        coords2 = self._to_vec3(coords2,"Coords2")
        return Vec3(
                min(coords1.x,coords2.x),
                min(coords1.y,coords2.y),
                min(coords1.z,coords2.z)
            ),Vec3(
                abs(coords1.x-coords2.x)+1,
                abs(coords1.y-coords2.y)+1,
                abs(coords1.z-coords2.z)+1
            )     
    def _to_vec3(self,coords,hit_txt):
        if coords is None:
            return self.hit(hit_txt)
        return Vec3(*coords)   

    def hit(self,txt):
        """The player hit a block and get the position of the block hit"""
        self.mc.postToChat(txt)
        self.mc.events.pollBlockHits()
        while True:
            for event in self.mc.events.pollBlockHits():

                pos=event.pos
                b=self.mc.getBlockWithData(pos)
                self.mc.setBlock(pos,41)
                sleep(0.2)
                self.mc.setBlock(pos,b)
                self.mc.postToChat("Block hit at "+str(pos))
                return pos


        
    def paste(self,data,coords,use_tqdm=False):
        coords = Vec3(*coords)
        dims = data.shape
        for y in tqdm(range(dims[1])) if use_tqdm else range(dims[1]):
            for z in range(dims[2]):
                for x in range(dims[0]):
                    block=data[y,z,x]
                    blockid=int(block)
                    blockdata=int((block-blockid)*100)
                    
                    self.mc.setBlock(coords.x+x,coords.y+y,coords.z+z,blockid,blockdata)
class Timer:

    def __init__(self):
        self.enabled = True
        self.tt=0
        self.reset()
    def reset(self):
        self.stt=self.tt=time.time()
    def print(self,txt):
        tt=time.time()
        if self.enabled:
            print("%07.3f %07.3f %s"%(tt-self.stt,tt-self.tt,txt))
        self.tt=tt
t=Timer()
t.enabled=False
# def __replace(txtFormat):
#     global _data
#     _data=0
#     _data=_data.replace(txtFormat.format(_old),txtFormat.format(_new))

# class Data(np.ndarray):
#     mc = None
#     # def ShapeBlocks(self):
#     #     lignes=self.data.splitlines()
#     #     coords=lignes[0].split(",")
#     #     dimsx=int(coords[0])
#     #     dimsy=int(coords[1])
#     #     dimsz=int(coords[2])
#     #     Shapeblocks=[]
#     #     for repeat in range(1):
#     #         idxligne=1
#     #         for y in range(dimsy):
#     #             idxligne=idxligne+1
#     #             for x in range(dimsx):
#     #                 ligne=lignes[idxligne]
#     #                 idxligne=idxligne+1
#     #                 donnee=ligne.split(",")
#     #                 for z in range(dimsz):
#     #                     blockid=donnee[z].split("/")
#     #                     if len(blockid)==1:
#     #                         blockdata=0
                            
#     #                     else:
#     #                         blockdata=int(blockid[1])
#     #                     Shapeblocks.append(ShapeBlock(x,y,z,int(blockid[0]),blockdata))
#     #     return Shapeblocks
    
#     # def replace(old,new):
#     #     global _data,_old,_new
#     #     _data,_old,_new=self.data,old,new
#     #     __replace("\n{}\n")
#     #     __replace("\n{},")
#     #     __replace(",{}\n")
#     #     __replace(",{},")
#     #     return Data(_data)

