
import tkinter as tk
import screen_utils  # Import the renamed utils for screen info
import logging
import logs.logging as logging_setup  # Import the existing logging module from logs directory

# Initialize logging system
log_file = logging_setup.initialize_logging()

def create_launcher_window():
    logging.info("Creating launcher window.")

    # Define the size of the window in inches
    window_width_inches = 8  # example width in inches
    window_height_inches = 6  # example height in inches

    logging.info(f"Desired window size: {window_width_inches}x{window_height_inches} inches.")

    # Convert inches to pixels based on the screen DPI
    try:
        dpi = screen_utils.get_screen_dpi()
        window_width_pixels = int(window_width_inches * dpi)
        window_height_pixels = int(window_height_inches * dpi)
        logging.info(f"Converted window size: {window_width_pixels}x{window_height_pixels} pixels.")
    except Exception as e:
        logging.error(f"Failed to convert window size: {e}")
        return

    # Create the main window
    root = tk.Tk()
    root.title("EcoSim Launcher")

    # Set window size
    root.geometry(f"{window_width_pixels}x{window_height_pixels}")

    # Center the window on the screen using screen_utils
    try:
        screen_utils.center_window(root, window_width_pixels, window_height_pixels)
        logging.info("Window centered on screen.")
    except Exception as e:
        logging.error(f"Failed to center window: {e}")

    # Enable resizing
    root.resizable(True, True)
    logging.info("Window is resizable.")

    # Start the Tkinter main loop
    logging.info("Starting Tkinter main loop.")
    root.mainloop()

if __name__ == "__main__":
    create_launcher_window()
