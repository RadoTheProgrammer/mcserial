
from sympy import use
from mcserial import MinecraftSerial
from mcserial.mcserial import t
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcs = MinecraftSerial(mc)
t.enabled=True
data=mcs.copy((102,1,15),(106,5,11),use_tqdm=True)