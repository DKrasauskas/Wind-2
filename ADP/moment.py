import main
import forces
import matplotlib.pyplot as plt
X = []
Y = []
Z = []
print(main.sensors_airfoil)
for y in range(0, len(main.aoa)):
    moment = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup, y , main.sensors_airfoil, 0.0)
    Y.append(moment[0])
    X.append(main.aoa[y])
    Z.append(moment[1])
plt.plot(X, Y)
plt.show()

