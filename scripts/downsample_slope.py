import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject
import os

def downsample_raster(input_path, output_path, resolution=10):
    with rasterio.open(input_path) as src:
        transform, width, height = calculate_default_transform(
            src.crs, src.crs, src.width, src.height, *src.bounds, resolution=resolution
        )

        kwargs = src.meta.copy()
        kwargs.update({
            'transform': transform,
            'width': width,
            'height': height,
            'compress': 'lzw'
        })

        with rasterio.open(output_path, 'w', **kwargs) as dst:
            reproject(
                source=rasterio.band(src, 1),
                destination=rasterio.band(dst, 1),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=src.crs,
                resampling=Resampling.average
            )

        print(f"Downsampled: {os.path.basename(output_path)}")

# File paths
base_dir = "data/processed/"
slope_input = os.path.join(base_dir, "slope.tif")
slope_output = os.path.join(base_dir, "slope_10m.tif")

downsample_raster(slope_input, slope_output)
