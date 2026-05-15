import scipy
# import scipy.constants as const


# A = Ampere
# C = Coulomb 
# H = Henry
# J = Joule
# K = Kelvin
# Pa = Pascal
PI = 3.141592653589793   # 3.1415926535897932384626433832795028

c = 299792458             # [m/s]        *Speed of Light in vacuum
e = eV = 1.602176634e-19  # [C],[J]      *Elementary charge, *Electron Volt (note: e ≠ eV) 
k = 1.380649e-23          # [J/K].       *Boltzmann constant 
N_A = 6.02214076e23       # [1/ mol]     *Avogadro constant 
h = 6.62607015e-34        # [J/Hz]       *Planck constant (for linear frequency, f)
h_bar = 1.054571817e-34   # [J*s]        reduced Planck constant  (for angular frequency, omega)
g_n = 9.80665             # [m/s^2]      *Standard acceleration of (Earth's) gravity 
atm = 101325              # [Pa]         *Standard atmosphere 
ssp = 100000              # [Pa]         *Standard-state pressure 
R = 8.314462618           # [J/(mol*K)]  *(Universal) molar gas constant

G = 6.67430e-11           # [(m^3)/(ks^2)]    Newtonian constant of gravitation  w/ std. uncert. = 0.000 15          e-11 (m^3)/(ks^2)
m_e = 9.1093837139e-31    # [kg]              Electron mass                      w/ std. uncert. = 0.000 000 0028    e-31 kg 
m_p = 1.67262192595e-27   # [kg]              Proton mass                        w/ std. uncert. = 0.000 000 000 52  e-27 kg
EP_0 = 8.8541878188e-12   # [F/m]             Vacuum electric permittivity       w/ std. uncert. = 0.000 000 0014    e-12 F/m
MU_0 = 1.25663706127e-6   # [N/A^2] or [H/m]  Vacuum magnetic permeability       w/ std. uncert. = 0.000 000 000 20  e-6  N/A^2

mu = 4 * PI * (10**-7)
ep = 1/ (MU_0 * (c**2)) 
EP = 1/ (mu * (c**2))

cc1 = 1 / (ep * 4 * PI)
cc2 = 1 / (4 * PI * EP_0)
cc3 = (MU_0 * (c**2))/ (4 * PI)

print("ep.  =", ep)
print("EP   =", EP)
print("EP_0 =", EP_0)
print("cc1 =", cc1)
print("cc2 =", cc2)
print("cc3 =", cc3)
# print(scipy.__version__)

#print(f"Speed of light (c): {const.c}")
#print(f"Pi: {const.pi}")

# Best Practice: Use the direct attribute variables
#epsilon_0 = const.epsilon_0
#mu_0 = const.mu_0

#print(f"Epsilon_0: {epsilon_0}")
#print(f"Mu_0: {mu_0}")

# Calculate Coulomb's constant
#k_e = 1 / (4 * const.pi * epsilon_0)
#print(f"Calculated k_e: {k_e}")




