import numpy as np
import os
#get experiment data
file = open("C:/Users/domin/OneDrive/Stalinis kompiuteris/ADP/input.txt", "r").read()
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
    ) for x in open("C:/Users/domin/OneDrive/Stalinis kompiuteris/ADP/airfoil.txt", "r").read().split("\n")
]).astype(float)

#get airfoil sensor locations
sensors_airfoil = np.stack([
    list(
        filter(
            len, 
            x.split("\t")
        )
    ) for x in open("C:/Users/domin/OneDrive/Stalinis kompiuteris/ADP/direct.txt", "r").read().split("\n")
]).astype(float)

#get wake sensor locations
sensors_wake = np.array([
    x for x in open("C:/Users/domin/OneDrive/Stalinis kompiuteris/ADP/wake.txt", "r").read().split("\n")
]).astype(float)

airfoil_sensors = file[:, 6:55]
wake_sensors = file[:, 55:103]
wake_sensors_static = file[:, 103:115]
aoa = file[:, 0]
q = file[:, -4]
rho = file[:, -6]