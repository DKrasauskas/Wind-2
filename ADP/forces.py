import main as mn
import numpy as np
import matplotlib.pyplot as plt
import math

#get to which sensor a specific point in the airfoil belongs to
def interpolate(airfoil_point, sensors):
    indices = []
    dist = 0xFFFFF
    index = -1
    for x in range(0, len(sensors)):
        dist_new = abs(abs(airfoil_point[0]) - abs(sensors[x, 0] * 0.01))
        if (dist_new < dist):
            if (sensors[x, 1] * airfoil_point[1] < 0 or sensors[x, 1] == 0) : continue
            dist = dist_new
            index = x  
    if index  == -1:
        if(airfoil_point[0] < 0.5) :
            indices.append(0)
        else:
            indices.append(48)
    else:
        indices.append(index)
    return indices

#relate airfoil points to sensor lookups
lookup = []
for x in mn.airfoil:  
    values = interpolate(x, mn.sensors_airfoil)
    lookup.append(values[0])

#do note dx is signed here to later on ease the force calculations
dx = list(mn.airfoil[1:, 0] - mn.airfoil[:-1, 0])
dy = list(mn.airfoil[1:, 1] - mn.airfoil[:-1, 1])
dx.append(dx[-1])
dy.append(dy[-1])

def get_Lift(data, dx, dy, lookup, it):
    Lift = 0
    Drag = 0
    for x in range(len(lookup)):
        if lookup[x] == -1: continue
        Lift += data[it, lookup[x]] * dx[x]
        Drag += data[it, lookup[x]] * dy[x]
    return (Lift, Drag)

def get_Moment(data, dx, dy, lookup, it, sensors, offset):
    Lift = 0
    Drag = 0
    LC = 0
    for x in range(len(lookup)):
        if lookup[x] == -1: continue
        Lift +=  data[it, lookup[x]] * dx[x] *(sensors[lookup[x], 0] * 0.01  - offset)
        LC +=  data[it, lookup[x]] * dx[x]
        Drag += data[it, lookup[x]] * dy[x] * sensors[lookup[x], 1] * 0.01    
    return (Lift + Drag, LC)

def get_cp_curve(data, sensors, q, it):
    Cp_upper = []
    Cp_lower = []
    X1 = []
    X2 = []
    for x in range(len(sensors)):
        if(sensors[x, 1] < 0):
            Cp_lower.append(data[it, x] / 247)
            X1.append(sensors[x, 0])
        else:
            Cp_upper.append(data[it, x] / 247)
            X2.append(sensors[x, 0])
    return(X1, Cp_lower, X2, Cp_upper)

CL =[]
CD = []
AoA = []

for x in range(len(mn.aoa)):
    c = get_Lift(mn.airfoil_sensors, dx, dy, lookup, x) / mn.q[x] 
    #convert to cl and cd:
    c_l = c[0] * math.cos(math.radians(mn.aoa[x])) - c[1] * math.sin(math.radians(mn.aoa[x]))
    c_d = c[1] * math.cos(math.radians(mn.aoa[x])) + c[0] * math.sin(math.radians(mn.aoa[x]))
    CL.append(c_l)
    CD.append(c_d)
    AoA.append(mn.aoa[x])
#can now visualize CL/CD using matplotlib



