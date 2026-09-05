# Figure plotting workflows

Code for Figures 2 and 6 of [Sharma, Arya, Cruz and Cleaves, *Automated
Exploration of Prebiotic Chemical Reaction Space: Progress and Perspectives*,
**Life** 2021, 11, 1140](https://www.mdpi.com/2075-1729/11/11/1140/htm).

Questions to Siddhant Sharma, siddhaantsharma.ss@gmail.com.

## Contents

| File | Contents |
|---|---|
| `Figure2.ipynb` | Mirror plot: FT-ICR-MS spectrum against the computed formose network |
| `Figure6_Generator.py` | Renders molecule SVGs and the node table for the Gephi plot |
| `39_Formose reaction_MeOH.csv` | FT-ICR-MS peak list, collected and analysed by [Huan Chen](https://nationalmaglab.org/component/maglabdata/?view=personnel&id=HuanChen) at the National High Magnetic Field Laboratory |
| `formose_output.txt` | Formose network products, generated with open-source graph-grammar tools |
| `Figure6_Data.csv` | Node table for Figure 6: SMILES and type |
| `formose_mirror_plot.png` | Figure 2 as published |

## Reproducing the figures

```bash
pip install -r requirements.txt
```

**Figure 2** — run `Figure2.ipynb`, or open it directly in the browser:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ssiddhantsharma/sharmaaryacruzcleaves2021/HEAD)

The spectra are negative-ESI, so the measured *m/z* is that of the [M−H]⁻ ion.
The notebook adds 1.007276 to recover the neutral mass before comparing with
the computed network.

**Figure 6** — needs Open Babel on the PATH, which is not a Python package:

```bash
conda install -c conda-forge openbabel   # or: apt install openbabel
python Figure6_Generator.py
```

This writes one SVG per molecule and an `imagen.csv` mapping table. Both are
inputs to [Gephi](https://gephi.org), where the network layout itself was made;
the figure is not produced end-to-end by this script.

The formose network can also be browsed interactively with
[mols2grid](https://github.com/cbouy/mols2grid).

## Licence

MIT, see `LICENSE`.
