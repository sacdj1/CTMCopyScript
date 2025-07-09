import shutil
import os

# === Configuration ===
source_file = '1.png'  # Replace with your actual file
destination_folder = './copies'  # Folder to store copied files
copy_count = 46

# === Ensure destination folder exists ===
os.makedirs(destination_folder, exist_ok=True)

# === Get file extension and base name ===
base_name, ext = os.path.splitext(os.path.basename(source_file))

# === Create the copies ===
for i in range(0, copy_count + 1):
    new_filename = f"{i}{ext}"
    new_filepath = os.path.join(destination_folder, new_filename)
    shutil.copy2(source_file, new_filepath)
    print(f"Created: {new_filepath}")
