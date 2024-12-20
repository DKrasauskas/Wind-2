import main
import forces
import matplotlib.pyplot as plt
import math
X = []
Y = []
Z = []

dynamicpressure = [
    247.1868982, 248.0168488, 247.7599522, 248.9852083, 249.2026075, 249.16308,
    251.1198703, 248.8271026, 243.8282517, 246.7324295, 244.7369547, 248.0366103,
    246.4755647, 246.5941169, 249.8548325, 245.6654943, 246.9300221, 247.503062,
    246.8114661, 246.1396742, 247.8389966, 244.8949981, 248.7480507, 242.7418633,
    244.2825932, 248.7282878, 245.2506046, 245.2308484, 245.6654943, 247.5228226,
    243.6702245, 249.1828438, 246.4162891, 246.4755647, 247.2264181, 245.4284125,
    246.0804005, 249.6967136, 252.4443718, 241.1223681, 246.6731525, 246.2779807,
    250.0722499, 242.3665919
]

print(main.sensors_airfoil)
for y in range(0, len(main.aoa)):
    moment = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup, y , main.sensors_airfoil, 0.0)
    Y.append(moment[0]/dynamicpressure[y])
    X.append(main.aoa[y]*math.pi /180)
    Z.append(moment[1])



plt.xlabel(r'Angle of Attack ($\alpha$) [rad]')
plt.ylabel(r'Moment coefficient ($C_m$) [-]')
plt.grid()
plt.axhline(linewidth = 1, color = "black")
plt.axvline(linewidth = 1, color = "black")
plt.plot(X, Y)
plt.show()

