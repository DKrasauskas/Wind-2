import main
import forces
import matplotlib.pyplot as plt
moment = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup,0 , main.sensors_airfoil, 0)
print(moment)

xcp = []
for y in range(1, len(main.aoa)):
    Mprev = 0xFFFF
    xc = -1
    arr = []
    p = []
    for x in range(0, 100):
        moment = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup, y , main.sensors_airfoil, x * 0.01)
        if(abs(Mprev) > abs(moment[0])):
            Mprev = moment[0]
            xc = x       
    xcp.append(xc)
plt.plot(main.aoa[1:], xcp)
plt.show()
print(xcp)

 