
import os
import subprocess

# Path to the create_zip.py script within the utils folder
create_zip_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'create_zip.py')

# Run the create_zip.py script
subprocess.run(['python', create_zip_script])
