# RNA Inverse Design -- GNN Research

**Role:** Graduate Assistant
**Advisor:** Prof. Amir Manzourolajdad
**Department:** Computer and Information Sciences, SUNY Polytechnic Institute
**Reference paper:** Secondary-Structure-Informed RNA Inverse Design via Relational Graph Neural Networks (Manzourolajdad & Mohebbi, MDPI 2025)

## Overview
Active research contribution on RNA inverse design -- designing sequences that fold into target secondary structures -- using a relational GNN architecture that encodes base-pair and structural graph features.

## My Contributions
- Run DSSR (v2.4.2) pipelines on PDB/mmCIF files to extract base pairs, helices, stems, loops, G-quadruplexes, pseudoknots, and torsion angles
- Prepare structural feature tensors for GNN training
- Coordinate AlphaFold-based structural validation of designed sequences
- Maintain reproducible computational notebooks aligned with research publication goals

## Key Tools
| Tool | Purpose |
|------|---------|
| DSSR v2.4.2 | RNA structural feature extraction from PDB/mmCIF |
| AlphaFold | Structural validation of designed sequences |
| PyTorch + PyG | Relational GNN training |
| Python (BioPython) | PDB parsing and preprocessing |

## DSSR Quick Reference
```bash
x3dna-dssr -i=file.pdb -o=out.txt
x3dna-dssr -i=file.pdb --json
x3dna-dssr -i=file.pdb --pair-only
x3dna-dssr -i=file.pdb --get-hbond
x3dna-dssr -i=file.pdb --more
```

## Tech Stack
Python, PyTorch, PyTorch Geometric, DSSR v2.4.2, AlphaFold, BioPython, NumPy
