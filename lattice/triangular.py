## Triangular lattice module

'''Triangular lattice module: Structure of triangular lattice'''

from math import *
import numpy as np

import lattice as ltc




'''Lattice structure'''


def ltcname():
    '''
    Lattice name
    '''
    return 'Triangular lattice'


def blvecs():
    '''
    Bravais lattice vectors
    '''
    return np.array([[0.,1.,0.],[sqrt(3.)/2.,1./2.,0.],[0.,0.,1.]])


def slvecs():
    '''
    Sublattice vectors
    '''
    return np.array([[0.,0.,0.]])


def pairs(r,Nbl,bc):
    '''
    The pairs between a lattice site r = [nr,sl] and itself, nearest neighbors, and second neighbors
    r=[nr,sl]: Lattice site index
    nr: Bravais lattice site index
    Nbl=[N1,N2,N3]: Bravais lattice dimension
    bc: Boundary condition
    '''
    nr=r[0]
    sl=r[1]

    # ONblite
    pairs0th=[[[nr,sl],[nr,sl]]]

    # Nearest neighbors
    pairs1st={
            0:[
                [[nr,0],[ltc.cyc(nr+np.array([-1,0,0]),Nbl,bc),0]],[[nr,0],[ltc.cyc(nr+np.array([0,-1,0]),Nbl,bc),0]],
                [[nr,0],[ltc.cyc(nr+np.array([1,-1,0]),Nbl,bc),0]],[[nr,0],[ltc.cyc(nr+np.array([1,0,0]),Nbl,bc),0]],
                [[nr,0],[ltc.cyc(nr+np.array([0,1,0]),Nbl,bc),0]],[[nr,0],[ltc.cyc(nr+np.array([-1,1,0]),Nbl,bc),0]]
                ]
            }

    # Second neighbors
    pairs2nd={
            0:[
                [[nr,0],[ltc.cyc(nr+np.array([-1,-1,0]),Nbl,bc),0]],[[nr,0],[ltc.cyc(nr+np.array([1,-2,0]),Nbl,bc),0]],
                [[nr,0],[ltc.cyc(nr+np.array([2,-1,0]),Nbl,bc),0]],[[nr,0],[ltc.cyc(nr+np.array([1,1,0]),Nbl,bc),0]],
                [[nr,0],[ltc.cyc(nr+np.array([-1,2,0]),Nbl,bc),0]],[[nr,0],[ltc.cyc(nr+np.array([-2,1,0]),Nbl,bc),0]]
                ]
            }

    return [pairs0th,pairs1st[sl],pairs2nd[sl]]


def hskpoints(uctype):
    '''
    High-symmetry points of the Brillouin zone
    '''
    if(uctype==111):
        return [['\u0393',pi*np.array([0.,0.,0.])],
                ['M',pi*np.array([2./sqrt(3.),0.,0.])],['M',pi*np.array([-1./sqrt(3.),1.,0.])],['M',pi*np.array([-1./sqrt(3.),-1.,0])],
                ['K',pi*np.array([0.,4./3.,0])],['K',pi*np.array([-2./sqrt(3.),-2./3.,0.])],['K',pi*np.array([2./sqrt(3.),-2./3.,0.])]]
    elif(uctype==211):
        return [['\u0393',pi*np.array([0.,0.,0.])],
                ['X\u2032',pi*np.array([-1./(2.*sqrt(3.)),1./2.,0.])],['Y\u2032',pi*np.array([sqrt(3.)/2.,1./2.,0.])],
                ['M\u2032',pi*np.array([1./sqrt(3.),1.,0.])],['M\u2032',pi*np.array([-2./sqrt(3.),0.,0.])]]
    elif(uctype==121):
        return [['\u0393',pi*np.array([0.,0.,0.])],
                ['X\u2032',pi*np.array([0.,1.,0.])],['Y\u2032',pi*np.array([1./sqrt(3.),0.,0.])],
                ['M\u2032',pi*np.array([1./sqrt(3.),1.,0])],['M\u2032',pi*np.array([-1./sqrt(3.),1.,0])]]
    elif(uctype==221):
        return [['\u0393',pi*np.array([0.,0.,0.])],
                ['M\u2032',pi*np.array([1./sqrt(3.),0.,0.])],['M\u2032',pi*np.array([-1./(2.*sqrt(3.)),1./2.,0.])],['M\u2032',pi*np.array([-1./(2.*sqrt(3.)),-1./2.,0])],
                ['K\u2032',pi*np.array([0.,2./3.,0])],['K\u2032',pi*np.array([-1./sqrt(3.),-1./3.,0.])],['K\u2032',pi*np.array([1./sqrt(3.),-1./3.,0.])]]
    elif(uctype==23231):
        return [['\u0393',pi*np.array([0.,0.,0.])],
                ['M\u2032',pi*np.array([0.,2./3.,0.])],['M\u2032',pi*np.array([-1./sqrt(3.),-1./3.,0.])],['M\u2032',pi*np.array([1./sqrt(3.),-1./3.,0])],
                ['K\u2032',pi*np.array([4./(3.*sqrt(3.)),0.,0])],['K\u2032',pi*np.array([-2./(3.*sqrt(3.)),2./3.,0.])],['K\u2032',pi*np.array([-2./(3.*sqrt(3.)),-2./3.,0.])]]




