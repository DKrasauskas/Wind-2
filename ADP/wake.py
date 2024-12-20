import main as mn
import matplotlib.pyplot as plt
import forces
import math
loc = mn.sensors_wake #locations
data = mn.wake_sensors #measurements

#compute dy:
dy = loc[1:47] - loc[0:46]
dF = 0
Y = []
X = []

#this yields the wake total pressure coefficient profiles at different aoa
for y in range(0, len(mn.aoa)):
    dF = 0
    for x in range(0, 46):
        c_pt = (data[y, x] / data[y, 47])
        
        dF -= c_pt ** 0.5 * (1 - c_pt ** 0.5) * dy[x] * 0.02
    Y.append(dF)
    X.append(mn.aoa[y]*math.pi/180)

aoaradlst = []

for i in range(0, len(mn.aoa)):
    aoarad = mn.aoa[i] * math.pi /180
    aoaradlst.append(aoarad)

plt.xlabel(r'Angle of Attack ($\alpha$) [rad]')
plt.ylabel(r'Something I dont know')
plt.grid()
plt.axhline(linewidth = 1, color = "black")
plt.axvline(linewidth = 1, color = "black")
plt.plot(aoaradlst, forces.CD, color = 'blue')
plt.plot(X, Y, color = 'red')
plt.show()

