
import os
import zipfile
from datetime import datetime
import shutil

# Paths and variables
archives_dir = os.path.join(os.getcwd(), '.archives')  # Path for .archives folder
utils_dir = os.path.join(os.getcwd(), 'utils')  # Path for utils folder
archive_enabled = True  # Control whether to save a copy in the .archives folder

# Ensure .archives folder creation (will only run when zipping)
def ensure_archives_folder():
    if archive_enabled:
        os.makedirs(archives_dir, exist_ok=True)

# Exclude directories and files based on guidelines
exclude_dirs = [archives_dir] + [os.path.join(os.getcwd(), d) for d in ['.local', '.openai', '.venv', '.env', '__pycache__', '.cache', '.config', '.github']]
exclude_files = [os.path.join(os.getcwd(), f) for f in ['.gitattributes', '.gitignore', 'LICENSE']]

# Function to save the zip file
def save_zip_file(destination_dir, zip_file_name):
    destination_path = os.path.join(destination_dir, zip_file_name)
    with zipfile.ZipFile(destination_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(os.getcwd()):
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
            for file in files:
                file_path = os.path.join(root, file)
                if file_path not in exclude_files:
                    arcname = os.path.relpath(file_path, start=os.getcwd())
                    zipf.write(file_path, arcname)
    return destination_path

# Example function that could be used in the future to create the zip files
def create_zip_files():
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    zip_file_name = f"EcoSim-{timestamp}.zip"

    # Ensure .archives folder exists if archiving is enabled
    ensure_archives_folder()

    # Save the zip file in the utils folder
    utils_zip_path = save_zip_file(utils_dir, zip_file_name)

    # Optionally save the zip file in the .archives folder
    if archive_enabled:
        archive_zip_path = save_zip_file(archives_dir, zip_file_name)

    return utils_zip_path

# The create_zip_files() function would be called to perform the zipping when needed


input("Press Enter to exit...")
