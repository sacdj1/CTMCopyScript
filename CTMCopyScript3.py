import os
import shutil
import re

# === Configuration ===
source_file = "1.png.mcmeta"   # Replace with your actual file
destination_folder = "./copies"
total_files = 46  # Total number of numbered files you want

# === Ensure destination folder exists ===
os.makedirs(destination_folder, exist_ok=True)

# === Detect the number in the filename ===
match = re.match(r"(\d+)(.*)", os.path.basename(source_file))
if not match:
    raise ValueError("Source filename must start with a number (e.g., '1.png.mcmeta').")

start_num = int(match.group(1))
rest_of_name = match.group(2)

# === Create copies up to the target number ===
for i in range(start_num, total_files + 1):
    new_filename = f"{i}{rest_of_name}"
    new_filepath = os.path.join(destination_folder, new_filename)
    shutil.copy2(source_file, new_filepath)
    print(f"Created: {new_filepath}")
