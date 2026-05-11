import dotenv
dotenv.load_dotenv(".env")
import os
import glob
import numpy as np
from gRNAde import gRNAde

gRNAde_module = gRNAde(split='multi', max_num_conformers=4, gpu_id=0)

pdb_files = glob.glob(r"C:\Users\mayan\structure-informed-RNA-inverse-design\data\*.pdb")
pdb_files = [f for f in pdb_files if '2CKY' not in f and '2HOL' not in f]

results = []

for pdb_file in pdb_files:
    pdb_name = os.path.basename(pdb_file)
    try:
        sequences, samples, perplexity, recovery, sc_score = gRNAde_module.design_from_pdb_file(
            pdb_filepath=pdb_file,
            output_filepath=None,
            n_samples=16,
            temperature=0.05,
            seed=0
        )
        avg_recovery = float(np.mean(recovery))
        avg_sc = float(np.mean(sc_score))
        results.append((pdb_name, avg_recovery, avg_sc))
        print(f"{pdb_name}: recovery={avg_recovery:.4f}, sc_score={avg_sc:.4f}")
    except Exception as e:
        print(f"{pdb_name}: ERROR - {e}")

results.sort(key=lambda x: x[1]+x[2], reverse=True)
print("\n=== TOP 10 PDB FILES BY RECOVERY + SC_SCORE ===")
for name, rec, sc in results[:10]:
    print(f"{name}: recovery={rec:.4f}, sc_score={sc:.4f}")