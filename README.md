### Figure Plotting Workflows
This repository holds the code used in [Sharma et al., 2021 Automated Exploration of Prebiotic Chemical Reaction Space: Progress And Perspectives](https://www.mdpi.com/2075-1729/11/11/1140/htm) to generate the Figure 2 and Figure 6. Using this material, one can replicate the figures created in our paper. Questions and feedback welcome! Please send any comments or questions to: Siddhant Sharma (siddhaantsharma.ss@gmail.com)

### Data Contents
1. NegESI_39_Formose_reaction_MeOH_Dual spray_Calmix_MIDAS.csv - MS-Data Collected and Analyzed by Huan Chen: (https://nationalmaglab.org/component/maglabdata/?view=personnel&id=HuanChen)
2. formose_output.txt - Generated Using Open Source Graph-Grammar Tools. The formose output can be explored interactively using: https://github.com/cbouy/mols2grid
3. Figure6_Data - Data For Gephi Plot.

### To reproduce the Figure 2 and Figure 6 in the main text of the paper:
1) Make sure all the dependencies are installed on your machine as mentioned in ```requirements.txt```
2) Run the Jupyter Notebook (.ipynb) for Figure 2 [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ssiddhantsharma/sharmaaryacruzcleaves2021/HEAD)
3) Execute ```$python Figure6_Generator.py``` for Figure 6.
In Figure 2, we corrected for the ESI effects while converting to 'mass' by adding 1.007276.

