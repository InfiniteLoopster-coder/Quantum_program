import numpy as np
import matplotlib.pyplot as plt
from qutip import destroy, fock, expect, wigner

# --------------------------
# PART 1: Compute Uncertainties
# --------------------------

# Define Hilbert space dimension (number of Fock states)
N = 20

# Create the annihilation operator for a harmonic oscillator
a = destroy(N)

# Define the position and momentum operators in natural units (ℏ = 1, m = 1, ω = 1):
#   x = (a + a†) / √2
#   p = i * (a† - a) / √2
x = (a + a.dag()) / np.sqrt(2)
p = 1j * (a.dag() - a) / np.sqrt(2)

# Get the ground state of the harmonic oscillator |0>
psi0 = fock(N, 0)

# Calculate expectation values for x and p (and their squares)
x_mean = expect(x, psi0)
x2_mean = expect(x * x, psi0)
p_mean = expect(p, psi0)
p2_mean = expect(p * p, psi0)

# Compute the standard deviations (uncertainties)
delta_x = np.sqrt(x2_mean - x_mean**2)
delta_p = np.sqrt(p2_mean - p_mean**2)

# Calculate the uncertainty product
uncertainty_product = delta_x * delta_p

# Print the results
print("Expectation value of x: {:.5f}".format(x_mean))
print("Expectation value of x^2: {:.5f}".format(x2_mean))
print("Standard deviation Δx: {:.5f}".format(delta_x))
print("Expectation value of p: {:.5f}".format(p_mean))
print("Expectation value of p^2: {:.5f}".format(p2_mean))
print("Standard deviation Δp: {:.5f}".format(delta_p))
print("Product Δx * Δp: {:.5f}".format(uncertainty_product))

# For the ground state of the harmonic oscillator in these units, you should obtain:
# Δx * Δp ≈ 0.5, which is the theoretical lower bound.

# --------------------------
# PART 2: Plotting the Wigner Function
# --------------------------

# The Wigner function provides a quasi-probability distribution in phase space (x, p).

# Define a grid for x and p values
xvec = np.linspace(-5, 5, 200)
pvec = np.linspace(-5, 5, 200)

# Compute the Wigner function for the ground state psi0
W = wigner(psi0, xvec, pvec)

# Plot the Wigner function using a filled contour plot
plt.figure(figsize=(8, 6))
plt.contourf(xvec, pvec, W, 100, cmap='RdBu_r')
plt.colorbar(label='Wigner function value')
plt.xlabel('x')
plt.ylabel('p')
plt.title("Wigner Function of the Ground State")
plt.show()

# --------------------------
# PART 3: Plotting the Analytical Position Probability Distribution
# --------------------------

# For the harmonic oscillator ground state in natural units, the analytical position-space wave function is:
#   ψ₀(x) = π^(-1/4) * exp(-x²/2)
# Therefore, the probability density is |ψ₀(x)|² = (1/√π) * exp(-x²).

x_analytical = np.linspace(-5, 5, 400)
psi0_x = (1 / np.pi**0.25) * np.exp(-x_analytical**2 / 2)

plt.figure(figsize=(8, 6))
plt.plot(x_analytical, psi0_x**2, label="|ψ(x)|² (analytical)", color='purple')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title("Position Probability Density for the Ground State")
plt.legend()
plt.show()
