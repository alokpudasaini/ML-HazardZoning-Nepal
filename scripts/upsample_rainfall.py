import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject
import os

def upsample_raster(input_path, output_path, resolution=10):
    with rasterio.open(input_path) as src:
        transform, width, height = calculate_default_transform(
            src.crs, src.crs, src.width, src.height, *src.bounds, resolution=resolution
        )

        kwargs = src.meta.copy()
        kwargs.update({
            'transform': transform,
            'width': width,
            'height': height
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

        print(f"Upsampled: {os.path.basename(output_path)}")

# File paths
base_dir = "data/processed/"
mean_input = os.path.join(base_dir, "mean_rainfall.tif")
max_input = os.path.join(base_dir, "max_rainfall.tif")

mean_output = os.path.join(base_dir, "rainfall_mean_10m.tif")
max_output = os.path.join(base_dir, "rainfall_max_10m.tif")

# Upsample both
upsample_raster(mean_input, mean_output)
upsample_raster(max_input, max_output)
