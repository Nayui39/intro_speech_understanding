import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    n = len(x) - 1
    indices = np.arange(n + 1)
    weighted_sum = np.dot(indices, x)
    total_sum = np.sum(x)
    return weighted_sum / total_sum if total_sum != 0 else 0

def matched_identity(x):
    n = len(x)
    return np.eye(n)

def sine_and_cosine(t_start, t_end, t_steps):
    t = np.linspace(t_start, t_end, t_steps)
    x = np.cos(t)
    y = np.sin(t)
    return t, x, y
