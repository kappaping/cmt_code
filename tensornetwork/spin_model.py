"""
Spin model module: Defines the quantum spin models.
"""


import numpy as np




def pauli_matrix(n):
    """
    Pauli matrix function: Defines the Pauli matrices.
    """

    if n==0:
        return np.array([[1., 0.], [0., 1.]])
    elif n==1:
        return np.array([[0., 1.], [1., 0.]])
    elif n==2:
        return np.array([[0., -1.j], [1.j, 0.]])
    elif n==3:
        return np.array([[1., 0.], [0., -1.]])


def tf_ising(J, hx, hz=0., N=2, bc="open"):
    """
    Transverse-field Ising chain: Define the Hamiltonian of the transverse-field Ising chain.
    """
    if N == 2:
        H = J * np.tensordot(pauli_matrix(3), pauli_matrix(3), axes=0) - (hx / 2) * (np.tensordot(pauli_matrix(1), pauli_matrix(0), axes=0) + np.tensordot(pauli_matrix(0), pauli_matrix(1), axes=0))
        H = np.moveaxis(H, [0, 2, 1, 3], [0, 1, 2, 3])

    return H



def heisenberg(J, Delta=1., N=2, set_real=True):
    """
    Heisenberg chain: Define the Hamiltonian of the Heisenberg chain.
    """
    Jis = (J / 4) * np.array([1, 1, Delta])
    if N == 2:
        H = sum([Jis[n - 1] * np.tensordot(pauli_matrix(n), pauli_matrix(n), axes=0) for n in [1, 2, 3]])
        H = np.moveaxis(H, [0, 2, 1, 3], [0, 1, 2, 3])
    if set_real:
        H = H.real

    return H




