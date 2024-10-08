# Michaelis-Menten vs. First-order Kinetics Simulation

This Python script compares **Michaelis-Menten** enzyme kinetics with **First-order elimination** using both **analytical** and **numerical** solutions. It solves the concentration over time and plots reaction rates versus concentration.

### Libraries Used:
- `NumPy`, `SciPy`, `Matplotlib`

### Key Models:
- **Michaelis-Menten**: Uses Lambert W function for analytical solution, `odeint` for numerical.
- **First-order Elimination**: Exponential decay for analytical, `odeint` for numerical.

### Constants:
- `K_m = 10.0`, `V_max = 50.0`, `C0 = 50.0`, `k = V_max / K_m`
- Time range: `t = np.linspace(0, 10, 100)`

### Functions:
- `michaelis_menten_lambert()`: Analytical solution with Lambert W function.
- `one_compartment_first_order()`: Analytical for first-order.
- `michaelis_menten_ode()`: Numerical ODE for Michaelis-Menten.
- `first_order_ode()`: Numerical ODE for first-order.
- Reaction rate calculation: `michaelis_menten_rate()` and `first_order_rate()`.

### Output:
4 subplots comparing numerical and analytical solutions of reaction rates:
1. Michaelis-Menten (Numerical vs Analytical)
2. First-order (Numerical vs Analytical)
3. Michaelis-Menten vs First-order (Analytical)
4. Michaelis-Menten vs First-order (Numerical)

### Run:
Install dependencies: `pip install numpy scipy matplotlib`
Execute the script: `python script_name.py`

Licensed under MIT.


First-order (Numerical vs. Analytical):
Compares numerical and analytical solutions for the First-order elimination model.

Michaelis-Menten vs. First-order (Analytical):
Compares analytical solutions for both models.

Michaelis-Menten vs. First-order (Numerical):
Compares numerical solutions for both models.

Each plot visualizes the reaction rate (v) against concentration (C), with proper axis limits set for clarity. The maximum reaction rate is capped at V_max to align with physical reality.

How to Run
Install required libraries:


pip install numpy scipy matplotlib
Run the script:

bash
Copy code
python script_name.py
The output will be displayed as a 2x2 grid of plots showing the reaction rate vs. concentration for both models.

License
This code is released under the MIT License. You are free to use, modify, and distribute the code.
