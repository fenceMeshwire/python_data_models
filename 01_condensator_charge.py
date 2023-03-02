#!/usr/bin/env python3

# Python 3.9.5

# 01_condensator_charge.py

# Dependencies
import matplotlib.pyplot as plt
import modsim
import numpy as np

def create_system():
    return modsim.System(U0=100, R=1e6, C=1e-6, t_0=0, t_end=8, dt=0.125)

def change_values(t, state, system):
    # state is currently not needed
    U0, R, C = system.U0, system.R, system.C
    return U0 * (1 - np.e**(-t/(R*C)))

def store_results(system, change_values):
    times_array = modsim.linrange(system.t_0, system.t_end, system.dt)
    n = len(times_array)

    series = modsim.TimeSeries(index=times_array)
    series.iloc[0] = system.t_0

    for i in range(n-1):
        t = times_array[i+1]
        state = series.iloc[i]
        series.iloc[i+1] = change_values(t, state, system)
    return series

def plot_results(results):

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(results, label='Voltage')
    ax.legend(loc='best')

    props = {
        'title':'Charging Curve of a Capacitor', 
        'xlabel':'Time (s)',
        'ylabel': 'Voltage (V)'
        }
    ax.set(**props)

    plt.show()

# 1. Create system
system = create_system()
# 2. Initialize the system
change_values(system.t_0, system.t_end, system)
# 3. Create and store the results
results = store_results(system, change_values)
# 4. Check the results
results
# 5. Plot the results
plot_results(results)
