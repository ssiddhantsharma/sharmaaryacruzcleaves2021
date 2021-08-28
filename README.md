### Figure Plotting
This repository holds the code used in Sharma et al., 2021 Automated Exploration of Prebiotic Chemical Reaction Space: Progress And Perspectives.to generate the Figure XX. Using this material, one can replicate the figure created in our paper.

Questions and feedback welcome! Please send any comments or questions to: Siddhant Sharma (siddhaantsharma.ss@gmail.com)

==========================
===CONTENTS
==========================
1.  - 
2.  -
3.  -

TO REPRODUCE THE FIGURE IN THE MAIN TEXT OF THE PAPER:
To generate Figures 1-4, run compute_h2s_so2_v14.py (i.e "python compute_h2s_so2_v14.py"). This script performs the equilibrium chemistry calculations, and plots the radiative transfer calculations. Note that before you can plot the RT calculations, you must run the radiative transfer code. You choose which plots are generated via the True/False switches in the code.

To generate Figure 5, run redox_calc.py.

TO PLOT THE FIGURES IN THE SI:
Run compute_henry_temp_salinity_v2.py to generate the figures showing temperature and salinity dependence of the Henry's Law constants for H2S and SO2 in the SI.
