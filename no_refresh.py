# %%



# %%
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
mc.conn.verbose_mode = False
pos = mc.player.getTilePos()




# %%
import time
def build():
    global n
    for x in range(dims[0]):
        for y in range(dims[1]):
            for z in range(dims[2]):
                if n%2:
                    b=b1
                else:
                    b=b2
                mc.setBlock(pos.x+x,pos.y+y,pos.z+z,b)
                n+=1

# %%
dims = (40,40,40)
b1 = block.DIAMOND_BLOCK.id
b2 = block.GOLD_BLOCK.id

mc.setBlocks(pos.x,pos.y,pos.z,pos.x+dims[0]-1,pos.y+dims[1]-1,pos.z+dims[2]-1,block.AIR.id)

# %%


# with mc.conn:
#     print(mc.conn.no_refresh)
#     n=0
#     print("preparing command...")
#     build()
#     print("sending command...")
#     print(mc.conn.no_refresh)
# print("done")
n=0
build()


# %%
mc.conn._send('world.setBlocks(56,5,57,95,44,96,0)\n')

# %%
mc.setBlock(pos.x,pos.y,pos.z,block.STONE.id)

# %%
cmd =mc.conn.no_refresh_cmd


# %%
cmd_str = cmd.decode()
cmd_bytes = cmd.encode()



# %%
with mc.conn:
    n=0
    build()

