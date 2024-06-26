## Face-centered cubic lattice module

'''Face-centered cubic lattice module: Lattice structure.'''

from math import *
import numpy as np

import lattice as ltc




'''Lattice structure'''


def ltcname():
    '''
    Lattice name
    '''
    return 'Face-centered cubic lattice'


def blvecs():
    '''
    Bravais lattice vectors
    '''
    return np.array([[0.,1.,0.],[sqrt(3.)/2.,1./2.,0.],[1/(2.*sqrt(3.)),1./2.,sqrt(2./3.)]])


def slvecs():
    '''
    Sublattice vectors
    '''
    return np.array([[0.,0.,0.]])




