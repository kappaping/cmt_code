## Band module

'''Band theory module: Setup of Hamiltonian in band theory'''

from math import *
import cmath as cmt
import numpy as np
import sympy
import joblib

import sys
sys.path.append('../lattice')
import lattice as ltc




def typeofbz(ltype,prds):
    '''
    Define the type of the Brillouin zone.
    '''
    # Rectangular Brillouin zone.
    if(ltype=='sq' or (prds[0]>1 and prds[1]==1) or (prds[0]==1 and prds[1]>1)):return 'rc'
    # Hexagonal Brillouin zone.
    elif(ltype in ['tr','ka']):return 'hx'


def ucblvecs(ltype,prds):
    '''
    Define the Bravais lattice vectors with periodicity prds.
    '''
    # Type of Brillouin zone.
    bztype=typeofbz(ltype,prds)
    # Bravais lattice vectors of original lattice.
    blvs=ltc.blvecs(ltype)
    # Lattice unrotated and preserves full symmetry
    if(max(prds)==1 or (max(prds)<20 and (ltype=='sq' or prds[0]==prds[1]))):return [prds[n]*blvs[n] for n in range(3)]
    # sqrt2 x sqrt2 on square lattice
    elif(ltype=='sq' and max(prds)==22):return [blvs[0]+blvs[1],-blvs[0]+blvs[1],blvs[2]]
    # n x 1 on lattices with triangular Bravais lattice
    elif(ltype in ['tr','ka'] and bztype=='rc'):
        if(np.argmax(np.array(prds))==0):return [(prds[0]/2.)*(-2*blvs[0]+blvs[1]),blvs[1],blvs[2]]
        elif(np.argmax(np.array(prds))==1):return [(prds[1]/2.)*(-1*blvs[0]+2*blvs[1]),blvs[0],blvs[2]]
    # sqrt3 x sqrt3 on lattices with triangular Bravais lattice
    elif(bztype=='hx' and max(prds)==23):return([blvs[0]+blvs[1],-blvs[0]+2*blvs[1],blvs[2]])
    # 2sqrt3 x 2sqrt3 on lattices with triangular Bravais lattice
    elif(bztype=='hx' and max(prds)==223):return([2*(blvs[0]+blvs[1]),2*(-blvs[0]+2*blvs[1]),blvs[2]])


def hskpoints(ltype,prds):
    '''
    List the high-symmetry points of the Brillouin zone.
    '''
    # Type of Brillouin zone.
    bztype=typeofbz(ltype,prds)
    # Bravais lattice vectors of unit cell.
    ucblvs=ucblvecs(ltype,prds)
    # Rectangular Brillouin zone.
    if(bztype=='rc'):
        [x,y]=[pi*np.cross(ucblvs[(n+1)%3],ucblvs[(n+2)%3])/np.dot(ucblvs[0],np.cross(ucblvs[1],ucblvs[2])) for n in range(2)]
        return [['\u0393',pi*np.array([0.,0.,0.])],['X',x],['Y',y],['M',x+y],['M',x-y]]
    # Hexagonal Brillouin zone.
    elif(bztype=='hx'):
        [m1,m2]=[pi*((-1)**(n+1))*np.cross(ucblvs[n],ucblvs[2])/np.dot(ucblvs[0],np.cross(ucblvs[1],ucblvs[2])) for n in range(2)]
        m3=-m1-m2
        return [['\u0393',pi*np.array([0.,0.,0.])],['M',m1],['M',m2],['M',m3],
                ['K',(2./3.)*(m2-m3)],['K',(2./3.)*(m3-m1)],['K',(2./3.)*(m1-m2)]]


def hskcontour(ltype,prds):
    '''
    Set the high-symmetry points in the Brillouin zone forming the contour for the band structure.
    '''
    # Type of Brillouin zone.
    bztype=typeofbz(ltype,prds)
    # All high-symmetry points of the Brillouin zone.
    hsks=hskpoints(ltype,prds)
    # Contour of rectangular Brillouin zone.
    if(bztype=='rc'):
        if(abs(np.linalg.norm(hsks[1][1])-np.linalg.norm(hsks[2][1]))<1e-14):return [hsks[0],hsks[1],hsks[3],hsks[0]]
        else:return [hsks[0],hsks[1],hsks[3],hsks[0],hsks[2],hsks[3],hsks[0]]
    # Contour of hexagonal Brillouin zone.
    elif(bztype=='hx'):return [hsks[0],hsks[1],[hsks[5][0],-hsks[5][1]],hsks[0]]


def listbz(ltype,prds,Nk,bzop=False):
    '''
    List the momenta in the Brillouin zone.
    '''
    # All high-symmetry points of the Brillouin zone.
    hsks=hskpoints(ltype,prds)
    # Number of side pairs.
    Nsdp=round((len(hsks)-1)/2)
    # Edge centers.
    kecs=[hsks[n+1][1] for n in range(Nsdp)]
    # List of momenta.
    ks=[]
    # If the Brillouin zone is open, exclude the momenta at one side.
    if(bzop==True): dkb=1e-13
    else: dkb=0.
    # Define a function which measures whether a momentum k is in the width of the Brillouin zone [-kec,kec].
    def inbzwidth(k,kec,dkb):
        return -np.linalg.norm(kec)**2-1e-14<np.dot(k,kec)<np.linalg.norm(kec)**2+1e-14-dkb
    # Edge centers of the Brillouin zone.
    kecs=[hsks[nsdp+1][1] for nsdp in range(Nsdp)]
    # List the momentum bounded by the Brillouin-zone edges.
    for n0 in np.linspace(-2.,2.,num=2*Nk+1):
        for n1 in np.linspace(-2.,2.,num=2*Nk+1):
            k=n0*kecs[0]+n1*kecs[1]
            if(np.array_equal(np.array([inbzwidth(k,((-1)**nsdp)*kecs[nsdp],dkb) for nsdp in range(Nsdp)]),np.array([1 for nsdp in range(Nsdp)]))):ks.append(k)
    # List of corners of momentum-space grids.
    dks=[(1./(2.*Nk))*hsks[Nsdp+1+nsdp][1] for nsdp in range(Nsdp)]
    return [ks,dks]







