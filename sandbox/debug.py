from mcserial import MinecraftSerial
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcs = MinecraftSerial(mc)
mcs.copy((101,1,16),(106,5,11))