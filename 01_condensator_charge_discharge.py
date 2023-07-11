#!/usr/bin/env python3

# Python 3.9.5

# 01_condensator_charge_discharge.py

# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_charging_results(U0=100, R=1e6, C=1e-6, t_0=0, t_end=8, dt=0.125):
    given_time = np.linspace(t_0, t_end, num=int(t_end/dt))
    given_current = {time:U0 * (1 - np.e**(-time/(R*C))) for time in given_time}
    return pd.Series(given_current)

def get_discharging_results(U0=100, R=1e6, C=1e-6, t_0=0, t_end=8, dt=0.125):
    given_time = np.linspace(t_0, t_end, num=int(t_end/dt))
    given_current = {time:U0 * (np.e**(-time/(R*C))) for time in given_time}
    return pd.Series(given_current)

def plot_results(charging, discharging):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(charging, label='Charging')
    ax.plot(discharging, label='Discharging')
    ax.legend(loc='best')
    
    props = {
        'title':'Charging/Discharging Curve of a Capacitor', 
        'xlabel':'Time (s)',
        'ylabel': 'Voltage (V)'
        }
    
    ax.set(**props)
    plt.show()

if __name__ == '__main__':
    charging = get_charging_results()
    discharging = get_discharging_results()
    plot_results(charging, discharging)
