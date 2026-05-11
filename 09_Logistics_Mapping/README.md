# Logistics Network Mapping

**Course:** DSA 506 Visual Analytics and Communications
**Dataset:** Synthetic US logistics network (warehouses, customers, routes)

## Overview
Geospatial analytics project mapping a US logistics network and analyzing warehouse coverage, route efficiency, and demand patterns using Folium interactive maps.

## Analyses
| Question | Visualization |
|----------|--------------|
| Warehouse coverage | Folium map with 150-mile radius circles |
| Route efficiency | Lines colored by threshold (under/over 200 miles) |
| Capacity utilization | Bubble map scaled by utilization % |
| Demand patterns | Dark-theme bubble map with priority quadrants |

## Key Feature
Haversine distance function for accurate geographic calculations between all node pairs.

## Files
| File | Description |
|------|-------------|
| `logistics_mapping.ipynb` | Full Python notebook |
| `customers.csv` | Customer locations and demand |
| `warehouses.csv` | Warehouse locations and capacity |
| `routes.csv` | Route assignments |

## Tech Stack
Python, Folium, Pandas, NumPy, Matplotlib, Jupyter/Colab
