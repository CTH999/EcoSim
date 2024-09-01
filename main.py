
import subprocess
import os

def run_launcher():
    # Path to the launcher.py script
    launcher_path = os.path.join(os.path.dirname(__file__), 'launcher.py')
    subprocess.run(['python', launcher_path])

if __name__ == "__main__":
    # Add any important background code here
    # ...

    # If double-clicked or run directly, it should start the launcher
    run_launcher()
