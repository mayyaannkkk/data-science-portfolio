import dotenv
dotenv.load_dotenv(".env")
import os
import numpy as np
from gRNAde import gRNAde

gRNAde_module = gRNAde(split='multi', max_num_conformers=4, gpu_id=0)

sequences, samples, perplexity, recovery_sample, sc_score = gRNAde_module.design_from_pdb_file(
    pdb_filepath = r"C:\Users\mayan\structure-informed-RNA-inverse-design\data\6E8T_1_A.pdb",
    output_filepath = r"C:\Users\mayan\structure-informed-RNA-inverse-design\data\6E8T_1_A_final_sequences.fasta",
    n_samples = 100,
    temperature = 0.05,
    seed = 0
)

print("Average recovery:", np.mean(recovery_sample))
print("Average sc_score:", np.mean(sc_score))
print("Total sequences:", len(sequences)-1)

for seq in sequences:
    print(seq.format('fasta'))