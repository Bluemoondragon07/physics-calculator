import scipy
import scipy.constants as const



print(scipy.__version__)

print(f"Speed of light (c): {const.c}")
print(f"Pi: {const.pi}")

# Best Practice: Use the direct attribute variables
epsilon_0 = const.epsilon_0
mu_0 = const.mu_0

print(f"Epsilon_0: {epsilon_0}")
print(f"Mu_0: {mu_0}")

# Calculate Coulomb's constant
k_e = 1 / (4 * const.pi * epsilon_0)
print(f"Calculated k_e: {k_e}")
