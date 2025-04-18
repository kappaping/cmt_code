# Self-complete python package for quantum materials/many-body lattice models
Since I started my postdoctoral stint at UC Berkeley, a significant portion of my research has been based on numerical computations of quantum many-body systems. To manage the codes for different projects harmoniously, I started to establish and maintain my own python package for the essential computations in theoretical condensed matter physics. My package is self-complete and is based only on the basic python packages, such as numpy, scipy, and sparse for matrix and tensor computations, as well as matplotlib (2D) and mayavi (3D) for graphics. This package has supported my broad exploration into various quantum many-body systems for diverse 1D, 2D, and 3D quantum materials.

The main features of my package include:
1. Public repository on GitHub: https://github.com/kappaping/cmt_code (modules for ongoing projects are private)
2. Wide applicability on arbitrary 1D to 3D lattices and Fermi-Hubbard models
3. Computation of band structures and superconducting/spin/charge ordered states:
  (1) Mean field: Hartree-Fock(-Bogoliubov) theory
  (2) Dynamics: Time-dependent Hartree-Fock(-Bogoliubov) theory
  (3) Beyond mean field: Functional renormalization group (RG), parquet RG
  (4) Classical Monte Carlo: Spin systems
4. 3D visualization of lattices and superconducting/spin/charge ordered states
