import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Define parameters
omega = 1.0  # frequency
tlist = np.linspace(0, 10, 100)  # time points

# Create basis states for a two-level system (qubit)
up = basis(2, 0)
down = basis(2, 1)

# Define the Hamiltonian for a simple two-level system
H = 0.5 * omega * sigmaz()

# Initial state: superposition of up and down states
psi0 = (up + down).unit()

# Solve the time-dependent Schrödinger equation
result = mesolve(H, psi0, tlist, [], [sigmax(), sigmay(), sigmaz()])

# Extract expectation values for visualization
sigmax_expect = result.expect[0]
sigmay_expect = result.expect[1]
sigmaz_expect = result.expect[2]

# Plot the expectation values
plt.figure(figsize=(8, 5))
plt.plot(tlist, sigmax_expect, label='⟨σx⟩')
plt.plot(tlist, sigmay_expect, label='⟨σy⟩')
plt.plot(tlist, sigmaz_expect, label='⟨σz⟩')
plt.xlabel('Time')
plt.ylabel('Expectation value')
plt.title('Time Evolution of a Qubit')
plt.legend()
plt.show()
