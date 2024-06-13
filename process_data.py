import os
from rh20t_api.extract import convert_rh20t

# Set these paths as environment variables to use the script

ROOT_DIR = os.environ.get("RH20T_ROOT")
DEPTH_DIR = os.environ.get("RH20T_DEPTH_ROOT")
DEST_DIR = os.environ.get("RH20T_DEST")
# ROOT_DIR = f"/mnt/share/nas/Other Datasets/rh20t/rgb_resized"
# DEPTH_DIR = f"/mnt/share/nas/Other Datasets/rh20t/depth"
# DEST_DIR = f"/mnt/share/nas/Other Datasets/rh20t/extract"

convert_rh20t(
    root_dir = ROOT_DIR,  
    dest_dir = DEST_DIR,
    depth_dir = DEPTH_DIR,
    num_workers = 200
)
