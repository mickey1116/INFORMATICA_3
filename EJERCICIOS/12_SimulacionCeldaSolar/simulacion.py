
from PropiedadesMaterialN import *
from PropiedadesMaterialP import *
from funcionesDeApoyo import *


def simulation(voltage):        #this function return j_cell of the solar cell
    # Built-in potential --------------------------------------------------------------
    V_bi = Vbi(Eg_n, Eg_p, chi_n, chi_p, N_d, N_a, Nc_n, Nc_p, Nv_n, Nv_p, ni_n, ni_p)

    # Depletion region ----------------------------------------------------------------
    x_n = region(N_a, N_d, eps_n, eps_p, N_d, N_a, V_bi, voltage )
    x_p = region(N_d, N_a, eps_n, eps_p, N_d, N_a, V_bi, voltage )

    if x_n > w_n:  # Condition in case the depletion region exceeds the width of the material
        x_n = w_n
        x_p = w_n * (N_d / N_a)

    # Photocurrent --------------------------------------------------------------------
    dj_p    =  dJp(s_p, L_p, D_p, w_n, x_n, alpha_1, Ref, Trans)
    dj_n    =  dJn(s_n, L_n, D_n, w_p, x_p, alpha_2, w_n, alpha_1, Ref, Trans)  
    dj_scr  =  dJscr(x_n, x_p, w_n, alpha_1, alpha_2 , Ref, Trans)
    j_ph    =  Jph(dj_n, dj_p, dj_scr)
    # Saturation current density J0 ---------------------------------------------------
    j0_p    =  J0pn(D_p, p_0, L_p, s_p, w_n, x_n)
    j0_n    =  J0pn(D_n, n_0, L_n, s_n, w_p, x_p)
    j_0     =  J0(j0_n, j0_p)
    # Saturation current density J00 --------------------------------------------------
    j_00    =  J00(x_n, x_p, ni_n, ni_p, L_p, L_n, D_p, D_n)
    # Dark current density ------------------------------------------------------------
    j_dark  =  Jdark(j_0, j_00, voltage)
    # Cell current density ------------------------------------------------------------
    j_cell  =  j_ph - j_dark
    return j_cell

# ========================Mi primera celda simulada========================
voltage = 0.5  #Voltios
j_celda = simulation(voltage)   #densidad de corriente que produce celda
pot_celda = voltage * j_celda   #densidad de potencia electrica producida por la celda

print("voltaje: ", voltage)
print("densidad de corriente: ", j_celda)
print("densidad de potencia: ", pot_celda)


# =======================Simulacion variando el voltaje====================
celdas=10
cells=[]
for u in range(celdas):
    cells.append(u)


amount_mcs = 1000
vol_high=0.5375
vol_low=0
step= -(vol_high-vol_low)/100

temps = np.arange(vol_high, vol_low, step)
current = np.zeros(shape=(len(temps), amount_mcs))
potential = np.zeros(shape=(len(temps), amount_mcs))

for a in range(len(cells)):
    for ind_v, voltage in enumerate(temps):
        for i in range(amount_mcs):
            current[ind_v, i] = simulation(voltage)
            potential[ind_v, i] = simulation(voltage)*voltage

print(temps)
tau = amount_mcs // 2
current_mean = np.mean(current[:, tau:], axis=1)
potential_mean = np.mean(potential[:, tau:], axis=1)

plt.figure()
plt.plot(temps, current_mean, label="Current")
plt.legend()
plt.xlabel(r"$Voltios$")
plt.ylabel(r"$\left<J\right>$")
plt.grid()
plt.show()

plt.figure()
plt.plot(temps, potential_mean, label="Current")
plt.legend()
plt.xlabel(r"$Voltios$")
plt.ylabel(r"$\left<J\right>$")
plt.grid()
plt.show()

V_mpp=0.4251
P_mpp=0.0159
J_mpp=P_mpp/V_mpp
J_sc=0.0424
def fill_Factor():
    return (J_mpp*V_mpp)/(vol_high*J_sc)

def efficience():
    return (J_sc*vol_high*fill_Factor())/(P_mpp)

print(fill_Factor())
print(efficience())