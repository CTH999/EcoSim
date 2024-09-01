
import tkinter as tk

def get_screen_size_inches():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    screen_width = root.winfo_screenwidth() / root.winfo_fpixels('1i')
    screen_height = root.winfo_screenheight() / root.winfo_fpixels('1i')
    root.destroy()
    return screen_width, screen_height

def get_screen_dpi():
    root = tk.Tk()
    dpi = root.winfo_fpixels('1i')
    root.destroy()
    return dpi

def center_window(root, window_width_pixels, window_height_pixels):
    dpi = get_screen_dpi()
    screen_width, screen_height = get_screen_size_inches()
    
    # Convert screen size to pixels
    screen_width_pixels = int(screen_width * dpi)
    screen_height_pixels = int(screen_height * dpi)
    
    # Calculate position for centering the window
    x_position = int((screen_width_pixels - window_width_pixels) / 2)
    y_position = int((screen_height_pixels - window_height_pixels) / 2)
    
    root.geometry(f"+{x_position}+{y_position}")
