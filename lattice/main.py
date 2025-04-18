## Main function

from math import *
import numpy as np
np.set_printoptions(threshold=np.inf)
import time
import joblib

import lattice as ltc


ltype='ch3d'
Nbl=[8,8,8]
rs=ltc.ltcsites(ltype,Nbl)[0]
bc=1

filet='../../data/lattice/checkerboard3d/888_bc_1'

NB,RD,RDV=ltc.ltcpairdist(ltype,rs,Nbl,bc,toread=False,filet=filet)
print(NB)
#print(RD)
#print(RDV)

joblib.dump([bc,NB,RD,RDV],filet)

