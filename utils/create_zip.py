import os
import zipfile
from datetime import datetime

def zipdir(path, ziph, exclude_dirs, exclude_files):
    # Zip the contents of the directory
    for root, dirs, files in os.walk(path):
        # Exclude directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        
        for file in files:
            file_path = os.path.join(root, file)
            # Exclude files
            if file_path not in exclude_files:
                arcname = os.path.relpath(file_path, start=path)
                ziph.write(file_path, arcname)

def create_zip():
    # Directories and files to exclude
    exclude_dirs = [os.path.join(os.getcwd(), d) for d in ['.local', '.openai', '.venv', '.env', '__pycache__', '.cache', '.config', '.github']]
    exclude_files = [os.path.join(os.getcwd(), f) for f in ['.gitattributes', '.gitignore', 'LICENSE']]

    # Zip file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    zip_file_name = f"EcoSim-{timestamp}.zip"
    
    # Create a zip file
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(os.getcwd(), zipf, exclude_dirs, exclude_files)
    
    print(f"Created zip file: {zip_file_name}")

if __name__ == "__main__":
    create_zip()
    input("Press Enter to exit...")  # Keeps the console window open
