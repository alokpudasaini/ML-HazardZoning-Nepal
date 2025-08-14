# Hazard Zoning in Nepal Using Unsupervised Clustering of Geospatial Data

## Overview
To assess relative hazard-prone areas in a region of Nepal using geospatial datasets (Slope, Soil Type, Vegetation, Rainfall) and unsupervised machine learning methods.
Using environmental factors that contribute to hazards like steep slopes, heavy rainfall, low vegetation, and weak soil. Three clustering algorithms (K-Means, DBSCAN, and Hierarchical) are applied to group pixels with similar characteristics. Resulting clusters were interpreted as low, medium, and high hazard zones.

## Data Sources
- **DSM**: [OpenTopography](https://portal.opentopography.org/)
- **Elevation**: [HDX Central Nepal DEM](https://data.humdata.org/)
- **Rainfall**: [CHIRPS-2.0](https://data.chc.ucsb.edu/products/CHIRPS-2.0/)
- **Soiltype**: Dijkshoorn JA and Huting JRM 2009. Soil and terrain database for Nepal. Report 2009/01 (available through: http://www.isric.org), ISRIC – World Soil Information, Wageningen (29 p. with data set)
- **Vegetation**: [MODIS MOD13Q1.061](https://lpdaac.usgs.gov/)
- **Landslide Inventory**: [Nepal Landslides Collection](https://umap.openstreetmap.fr/)

*(See `/data/README.md` for details on licensing and preprocessing.)*

## License
This project is licensed for research and educational use only.  
If you use this project in your research or publications, please cite:

Pudasaini, A. (2025). Landslide Risk Prediction in Nepal using Satellite & Open GIS Data. GitHub repository. https://github.com/alokpudasaini/ML-Landslide-Nepal


