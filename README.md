# Landslide Risk Prediction in Nepal using Satellite & Open GIS Data

## Overview
This project uses publicly available geospatial datasets and machine learning to identify landslide-prone areas in Nepal.  
Features include elevation, slope, rainfall, soil type, and vegetation indices.  
The goal is to produce a high-resolution landslide risk map for academic and policy use.

## Data Sources
- **DSM**: [OpenTopography](https://portal.opentopography.org/)
- **Elevation**: [HDX Central Nepal DEM](https://data.humdata.org/)
- **Rainfall**: [CHIRPS-2.0](https://data.chc.ucsb.edu/products/CHIRPS-2.0/)
- **Soil**: ISRIC World Soil Information
- **Vegetation**: [MODIS MOD13Q1.061](https://lpdaac.usgs.gov/)
- **Landslide Inventory**: [Nepal Landslides Collection](https://umap.openstreetmap.fr/)

*(See `/data/README.md` for details on licensing and preprocessing.)*

## Methods
1. **Data Preparation** – Align all datasets to a 10 m grid (slope raster as reference).
2. **Label Creation** – Rasterize historical landslides (points & polygons).
3. **Feature Stacking** – Combine slope, elevation, rainfall, soil, and NDVI.
4. **Model Training** – Random Forest / XGBoost classification.
5. **Evaluation** – Precision, recall, F1-score, ROC-AUC.
6. **Risk Mapping** – Generate a probability raster of landslide occurrence.

## License
This project is licensed for research and educational use only.  
If you use this project in your research or publications, please cite:

Pudasaini, A. (2025). Landslide Risk Prediction in Nepal using Satellite & Open GIS Data. GitHub repository. https://github.com/alokpudasaini/ML-Landslide-Nepal


