Heisenberg Uncertainty Principle Simulation with QuTiP
This project demonstrates a simulation of the Heisenberg uncertainty principle using Python and the QuTiP library. The code computes the uncertainties (standard deviations) of the position and momentum operators for the ground state of the harmonic oscillator, verifies that their product meets the theoretical lower bound, and provides visualizations using plots.

Overview
In quantum mechanics, the Heisenberg uncertainty principle states that the product of the uncertainties in position and momentum cannot be arbitrarily small. For the ground state of the quantum harmonic oscillator (a minimum uncertainty state), the product is exactly 0.5 (in natural units where ℏ = 1).


This project uses QuTiP to:

Compute expectation values and uncertainties for the position and momentum operators.
Calculate the uncertainty product Δ𝑥Δ𝑝

Visualize the quantum state using:
A Wigner function plot (phase-space representation).
A plot of the analytical position probability distribution ∣𝜓(𝑥)∣2


Features
Computation of Uncertainties:
Calculates the expectation values of position and momentum operators, their squares, and derives the standard deviations.

Verification of the Uncertainty Principle:
Displays the uncertainty product Δ𝑥Δ𝑝 for the harmonic oscillator ground state.

Visualization:
Wigner Function: A contour plot showing the phase-space distribution of the quantum state.
Position Probability Distribution: A plot of the Gaussian probability density ∣𝜓(𝑥)∣2 for the ground state.

![Screenshot 2025-02-07 084244](https://github.com/user-attachments/assets/590358b5-7633-4f3a-b845-6b168f0d01c4)


