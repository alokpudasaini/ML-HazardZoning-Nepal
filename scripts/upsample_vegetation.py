import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject
import os

# Input and output file paths
input_path = "data/processed/vegetation_rescaled.tif"
output_path = "data/processed/vegetation.tif"

# Target resolution (10 meters per pixel)
target_resolution = 10

with rasterio.open(input_path) as src:
    # Calculate the transform and new dimensions for 10m resolution
    transform, width, height = calculate_default_transform(
        src.crs, src.crs, src.width, src.height, *src.bounds, resolution=target_resolution
    )

    kwargs = src.meta.copy()
    kwargs.update({
        'crs': src.crs,
        'transform': transform,
        'width': width,
        'height': height,
        'resampling': Resampling.nearest
    })

    with rasterio.open(output_path, 'w', **kwargs) as dst:
        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=src.crs,
            resampling=Resampling.nearest
        )

print("Vegetation data resampled to 10m and saved to:")
print(output_path)
