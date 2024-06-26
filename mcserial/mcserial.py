#from minecraftstuff import ShapeBlock,MinecraftShape

import time

from mcpi.minecraft import Vec3,Minecraft
#from mcpi.timer import t
from time import sleep
import numpy as np
from tqdm import tqdm
class MinecraftSerial:
    def __init__(self,mc:Minecraft):
        self.mc=mc
    

    def copy(self,coords1=None,coords2=None,show_progress=True):
        #t.reset()
        coords,dims = self._copy_util(coords1,coords2)

        data=np.zeros((dims.y,dims.z,dims.x))#,dtype=np.float16)
        #t.print("setup")
        
        def _copy():
            for y in range(dims.y):
                for z in range(dims.z):
                    for x in range(dims.x):
                        #t.print("start")
                        block=self.mc.getBlockWithData(coords.x+x,coords.y+y,coords.z+z)
                        data[y,z,x]=block.id+block.data/100
                        #t.print("getBlockWithData")
                        update_func()
                        #t.print("updated")
                    #t.print("z")
        if show_progress:
            with tqdm(total=dims.y*dims.z*dims.x) as pbar:
                update_func=lambda: pbar.update(1)
                _copy()
                return data
        else:
            update_func=lambda: None
            _copy()
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
                # b=self.mc.getBlockWithData(pos)
                # self.mc.setBlock(pos,41)
                # sleep(0.2)
                # self.mc.setBlock(pos,b)
                self.mc.postToChat("Block hit at "+str(pos))
                return pos


        
    def paste(self,data,coords=None,show_progress=False):
        coords = self._to_vec3(coords,"Coords")
        dims = data.shape
        def _paste():
            for y in range(dims[0]):
                for z in range(dims[1]):
                    for x in range(dims[2]):
                        block=data[y,z,x]
                        blockid=int(block)
                        blockdata=round((block-blockid)*100)
                        print(blockdata)
                        self.mc.setBlock(coords.x+x,coords.y+y,coords.z+z,blockid,blockdata)
                        update_func()
        if show_progress:
            with tqdm(total=dims[1]*dims[2]*dims[0]) as pbar:
                update_func=lambda: pbar.update(1)
                _paste()
        else:
            update_func=lambda: None
            _paste()

    save = staticmethod(np.save)
    load = staticmethod(np.load)

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

