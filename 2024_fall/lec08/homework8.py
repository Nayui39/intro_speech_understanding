import numpy as np

def dft_matrix(N):
    W = np.zeros((N, N), dtype=complex)
    j = 0 + 1j
    for k in range(N):
        for n in range(N):
            W[k, n] = np.cos(2 * np.pi * k * n / N) - j * np.sin(2 * np.pi * k * n / N)
    return W
