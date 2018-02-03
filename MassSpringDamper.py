#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import numpy as np
import random
from scipy.integrate import odeint
from numpy import arange



class MassSpringDamper:
    def __init__(self, m, k, c):
        self.m = m
        self.k = k
        self.c = c

    def simulate(self, x, x_dot, t=100.0, dt=0.01):
        initial_state = [x, x_dot]
        times = arange(0.0, t, dt)  # Set the simulation timesteps
        # Do the simulation
        state = odeint(lambda s,t: self.equation(s, t), initial_state, times)
        # Return    the states (as [x, x_dot]) and the simulation timesteps
        return state,times

    # This function takes the current state [x, x_dot] and returns the
    # next velocity and acceleration [x_dot and x_dot_dot].  The
    # function is used by the scipy ode solver.
    def equation(self, state, t):
        # unpack the state vector
        x = state[0]
        x_dot = state[1]
        # compute acceleration xdd
        x_dot_dot = -self.k / self.m * x - self.c / self.m * x_dot
        return [x_dot, x_dot_dot]

def plot_msd():
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
    state, t = smd.simulate(0.0, 1.0)
    axes = plt.gca()
    axes.set_xlim([0, 100])
    axes.set_ylim([-1.0, 1.0])
    plt.yticks(np.arange(-1.0, 1.25, 0.25))
    plt.title('Displacement-time plot')
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.plot(t, state[:, 0])
    plt.show()
