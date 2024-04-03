# %%

from mcserial import MinecraftSerial
#from mcpi.timer import Timer
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcs = MinecraftSerial(mc)


# %%

data=mcs.load("house.npy")
# %%
mcs.paste(data)