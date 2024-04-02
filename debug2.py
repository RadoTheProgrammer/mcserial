# %%
from mcserial import MinecraftSerial
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcs = MinecraftSerial(mc)

# %%
data=mcs.copy((101,1,16),(106,5,11))
data

# %%
import numpy as np
data2 = data.view(np.ndarray)

# %%
mc.setBlock(mcs.hit("test"),31,1)


