modules = [
    'dotenv', 'wandb', 'torch', 'torch_geometric', 'torch_scatter',
    'torch_cluster', 'sklearn', 'cpdb', 'torchmetrics', 'MDAnalysis',
    'einops', 'ml_collections', 'Bio', 'biotite', 'draw_rna',
    'gdown', 'yaml', 'tqdm'
]

for m in modules:
    try:
        __import__(m)
        print(f"OK: {m}")
    except ImportError as e:
        print(f"MISSING: {m} -> {e}")