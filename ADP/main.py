import numpy as np
import os
#get experiment data
file = open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Newcode/Wind-2/ADP/input.txt", "r").read()
file = file.replace(",", ".")
file = np.stack([
        list(
            filter(
                lambda x : x != "L",
                x.split("\t") 
            ) 
        )
        for x in file.split("\n")
]).astype(float)

#get airfoil 
airfoil = np.stack([
    list(
        filter(
            len, 
            x.split(" ")
        )
    ) for x in open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Newcode/Wind-2/ADP/airfoil.txt", "r").read().split("\n")
]).astype(float)

#get airfoil sensor locations
sensors_airfoil = np.stack([
    list(
        filter(
            len, 
            x.split("\t")
        )
    ) for x in open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Newcode/Wind-2/ADP/direct.txt", "r").read().split("\n")
]).astype(float)

#get wake sensor locations
sensors_wake = np.array([
    x for x in open("C:/Users/seppe/OneDrive - Delft University of Technology/Documents/0 - University/Bcs AE/Bsc AE2/AE2130-II Low Speed Windtunnel Test/GitHub/Newcode/Wind-2/ADP/wake.txt", "r").read().split("\n")
]).astype(float)

airfoil_sensors = file[:, 6:55]
wake_sensors = file[:, 55:103]
wake_sensors_static = file[:, 103:115]
aoa = file[:, 0]
q = file[:, -4]
rho = file[:, -6]