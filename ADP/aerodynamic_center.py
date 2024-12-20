import main
import forces

moment = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup,0 , main.sensors_airfoil, 0)
print(moment)

dM_prev = 0xFFFF
xcp = -1
for p in range(0, 100):
    x = p /100 
    dM = 0
    M_prev = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup, 0, main.sensors_airfoil, x)[0]
    for y in range(1, len(main.aoa)):
        moment = forces.get_Moment(main.airfoil_sensors, forces.dx, forces.dy, forces.lookup, y , main.sensors_airfoil, x)
        dM += M_prev - moment[0]
        M_prev = moment[0]
    if(abs(dM) < abs(dM_prev)):
        dM_prev = dM
        xcp = x
    print(xcp)