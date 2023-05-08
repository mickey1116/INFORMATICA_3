import numpy as np
import matplotlib.pyplot as plt

k=1
r = 1
T = 0.01
q = 1
elec_Circunferenciales = 3
elec_Internos = 2

def crear_Estado_Inicial():
    angulo = 6.28/(elec_Circunferenciales)
    x_out = [r*np.cos(ang) for ang in np.arange(0, 6.28, angulo)]
    y_out = [r*np.sin(ang) for ang in np.arange(0, 6.28, angulo)]
    x_in = [np.random.random() - 0.5 for i in range(elec_Internos)]
    y_in = [np.random.random() - 0.5 for i in range(elec_Internos)]
    return x_out,y_out,x_in,y_in

def dibujar_sistema(x_out,y_out,x_in,y_in):
    plt.figure()
    plt.plot(x_out,y_out, "ro")
    plt.plot(x_in, y_in, "bo")
    plt.gca().set_aspect("equal")
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.grid()
    plt.show()

x_out,y_out, x_in,y_in = crear_Estado_Inicial()
dibujar_sistema(x_out,y_out,x_in,y_in)

r=[]
for i in range(len(x_out)):
    r.append((x_out[i], y_out[i]))
for i in range(len(x_in)):
    r.append((x_in[i], y_in[i]))

print( "======", r)
def distancia(r1, r2):
    return ((r1[0]-r2[0]) ** 2 + (r1[1]-r2[1])**2) ** 0.5

from itertools import combinations
def calcular_energia_total():
    sumEnergias = 0
    combinaciones = list(combinations(r, 2))
    for r_ in combinaciones:
        r1, r2 = r_[0], r_[1]
        #print(r1,"vs", r2, "distancia =>", distancia(r1,r2))
        sumEnergias += k*q*q / distancia(r1,r2)
    #print("final",sumEnergias)
    return sumEnergias


calcular_energia_total()


def metropolis(ran_int_position):  #cambio aleatorio de la posicion de un electron interno
    r.pop(ran_int_position)
    x_change = np.random.random() - 0.5
    y_change = np.random.random() - 0.5
    r.append((x_change,y_change))
    x_in.pop(int(ran_int_position-elec_Circunferenciales))
    y_in.pop(int(ran_int_position-elec_Circunferenciales))
    x_in.append(x_change)
    y_in.append(y_change)
    calcular_energia_total()


def paso_montecarlo(T):
    for i in range(elec_Internos):
        ran_int_position=np.random.randint(0,len(r))
        while ran_int_position < elec_Circunferenciales:
            ran_int_position=np.random.randint(0,len(r))
        else: pass
        metropolis(ran_int_position)
    #dibujar_sistema(x_out,y_out,x_in,y_in)

amount_mcs = 1000
T_high=5
T_low=0.01
step=-0.1

def random_configuration():
    ran_int_position=np.random.randint(0,len(r))
    while ran_int_position < elec_Circunferenciales:
        ran_int_position=np.random.randint(0,len(r))
    else: pass


temps = np.arange(T_high, T_low, step)
energies = np.zeros(shape=(len(temps), amount_mcs))
random_configuration()


for ind_T, T in enumerate(temps):
    for i in range(amount_mcs):
        paso_montecarlo(T)
        energies[ind_T, i] = calcular_energia_total()


tau = amount_mcs // 2
energy_mean = np.mean(energies[:, tau:], axis=1)

plt.figure()
plt.plot(temps, energy_mean, label="Energy")
plt.legend()
plt.xlabel(r"$T$")
plt.ylabel(r"$\left<E\right>$")
plt.grid()
plt.show()

print(x_out)
print(y_out)
print(x_in)
print(y_in)
print(temps)
dibujar_sistema(x_out,y_out,x_in,y_in)
