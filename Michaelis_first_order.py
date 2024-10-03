import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw
from scipy.integrate import odeint

# Constants for Michaelis-Menten model (choose K_m > 0 and V_max > 0)
K_m = 10.0   # Michaelis constant
V_max = 50.0  # Maximum reaction rate

# Constant for first-order elimination model
k = V_max / K_m  # First-order rate constant derived from Michaelis-Menten at low concentrations

# Time points for simulation
t = np.linspace(0, 10, 100)

# Initial concentration
C0 = 50.0

# Corrected Michaelis-Menten model using Lambert W function (Analytical solution)
def michaelis_menten_lambert(t, C0, V_max, K_m):
    # Corrected analytical formula with Lambert W function
    term = (C0 / K_m) * np.exp((C0 - V_max * t) / K_m)
    W = lambertw(term)
    C_t = K_m * W.real
    return C_t

# One-compartment model with first-order elimination (Analytical solution)
def one_compartment_first_order(t, C0, k):
    return C0 * np.exp(-k * t)

# Corrected numerical solver for Michaelis-Menten model
def michaelis_menten_ode(C, t, V_max, K_m):
    return -V_max * C / (K_m + C)

# Solve first-order numerically
def first_order_ode(C, t, k):
    return -k * C

# Solve ODEs numerically using odeint
C_mm_numerical = odeint(michaelis_menten_ode, C0, t, args=(V_max, K_m)).flatten()
C_first_order_numerical = odeint(first_order_ode, C0, t, args=(k,)).flatten()

# Analytical solutions
C_mm_analytical = michaelis_menten_lambert(t, C0, V_max, K_m)
C_first_order_analytical = one_compartment_first_order(t, C0, k)

# Reaction rate calculations
def michaelis_menten_rate(C, V_max, K_m):
    return V_max * C / (K_m + C)

def first_order_rate(C, k):
    return k * C

# Calculate reaction rates for both models
rate_mm_analytical = michaelis_menten_rate(C_mm_analytical, V_max, K_m)
rate_mm_numerical = michaelis_menten_rate(C_mm_numerical, V_max, K_m)
rate_first_order_analytical = first_order_rate(C_first_order_analytical, k)
rate_first_order_numerical = first_order_rate(C_first_order_numerical, k)

# Plotting the results in 4 subplots for reaction rate vs concentration

plt.figure(figsize=(12, 12))

# 1st subplot: Michaelis-Menten (Numerical vs Analytical) - Reaction rate vs Concentration
plt.subplot(2, 2, 1)
plt.plot(C_mm_numerical, rate_mm_numerical, 'b--', label='Michaelis-Menten (Numerical)', linewidth=2)
plt.plot(C_mm_analytical, rate_mm_analytical, 'k-', label='Michaelis-Menten (Analytical)', linewidth=2)
plt.xlabel('Concentration (C)')
plt.ylabel('Reaction Rate (v)')
plt.title('Michaelis-Menten (Numerical vs Analytical)')
plt.xlim(0, 50)  # Adjust x-axis limits
plt.ylim(0, V_max)  # Adjust y-axis limits (since max reaction rate is V_max)
plt.legend()
plt.grid(True)

# 2nd subplot: First-order (Numerical vs Analytical) - Reaction rate vs Concentration
plt.subplot(2, 2, 2)
plt.plot(C_first_order_numerical, rate_first_order_numerical, 'g--', label='First-order (Numerical)', linewidth=2)
plt.plot(C_first_order_analytical, rate_first_order_analytical, 'r-', label='First-order (Analytical)', linewidth=2)
plt.xlabel('Concentration (C)')
plt.ylabel('Reaction Rate (v)')
plt.title('First-order (Numerical vs Analytical)')
plt.xlim(0, 50)  # Adjust x-axis limits
plt.ylim(0, V_max)  # Adjust y-axis limits for first-order
plt.legend()
plt.grid(True)

# 3rd subplot: Michaelis-Menten vs First-order (Analytical) - Reaction rate vs Concentration
plt.subplot(2, 2, 3)
plt.plot(C_mm_analytical, rate_mm_analytical, 'k-', label='Michaelis-Menten (Analytical)', linewidth=2)
plt.plot(C_first_order_analytical, rate_first_order_analytical, 'r-', label='First-order (Analytical)', linewidth=2)
plt.xlabel('Concentration (C)')
plt.ylabel('Reaction Rate (v)')
plt.title('Michaelis-Menten vs First-order (Analytical)')
plt.xlim(0, 50)  # Adjust x-axis limits for low concentration
plt.ylim(0, V_max)  # Reaction rate max is V_max
plt.legend()
plt.grid(True)

# 4th subplot: Michaelis-Menten vs First-order (Numerical) - Reaction rate vs Concentration
plt.subplot(2, 2, 4)
plt.plot(C_mm_numerical, rate_mm_numerical, 'b--', label='Michaelis-Menten (Numerical)', linewidth=2)
plt.plot(C_first_order_numerical, rate_first_order_numerical, 'g--', label='First-order (Numerical)', linewidth=2)
plt.xlabel('Concentration (C)')
plt.ylabel('Reaction Rate (v)')
plt.title('Michaelis-Menten vs First-order (Numerical)')
plt.xlim(0, 50)  # Adjust x-axis limits
plt.ylim(0, V_max)  # Max reaction rate should not exceed V_max for MM
plt.legend()
plt.grid(True)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
