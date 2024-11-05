# Projeto mancal hidrodinamico
import math
d=0.784
r=d/2
w=500 #rpm
e=0.85
rymed=-2120.53
ryalt=-192.78
rymed=167.56
ryalt=15.23
Rm=0.00000197
On = 30
P = ((rymed + ryalt)**2 + (rymed + ryalt)**2) ** 0.5
P = P * 0.224809

U = 2 * math.pi * r * w / 60
Cd= 0.0012 * d
Cr= Cd/2
L = d * 0.5
Ke= On/(math.pi *4)
n = (P * Cr)/(Ke * U * L**3)

pmed = P/(L*d)  
fi  = math.atan((math.pi * (1-e**2)**0.5)/4*e)

Ts = n*d**3*L*n*math.pi**2/(Cd * (1-e**2)*0.5)
Tr = Ts + P * e * math.sin(fi)

mi = 2*Tr/(P*d)

hmin = Cr * (1-e)

hminnew = 4*Rm
enew    = 1-hminnew/Cr
ONnew   = 100
Kenew   = ONnew/(4 * math.pi)
Pnew    = n*Kenew*U*L**3/Cr*2

Nmh     = Pnew/P