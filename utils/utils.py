
import json
import os
import tkinter as tk
from screeninfo import get_monitors

def get_screen_resolution():
    """
    Get the screen resolution (width, height) in pixels of the monitor where
    the majority of the window is displayed.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def get_monitor_physical_size():
    """
    Get the physical size of the monitor in millimeters (width, height).
    """
    monitors = get_monitors()
    primary_monitor = monitors[0]
    width_mm = primary_monitor.width_mm
    height_mm = primary_monitor.height_mm
    return width_mm, height_mm

def load_conversion_data(json_file='utils/conversion_data.json'):
    """
    Load the conversion data from a JSON file.
    
    :param json_file: Path to the JSON file.
    :return: Dictionary containing the conversion data.
    """
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"JSON file '{{json_file}}' not found.")
    
    with open(json_file, 'r') as file:
        conversion_data = json.load(file)
    return conversion_data

def convert_to_millimeters(x, y, unit, conversion_data):
    """
    Convert the given dimensions (x, y) in the specified unit to millimeters.
    
    :param x: The width dimension.
    :param y: The height dimension.
    :param unit: The unit of measurement (e.g., 'in', 'cm', 'mm', 'ratio').
    :param conversion_data: The dictionary containing the conversion equations.
    :return: Tuple (width_mm, height_mm) representing the dimensions in millimeters.
    """
    if unit == 'ratio':
        # Handle ratio as a special case
        screen_width, screen_height = get_screen_resolution()
        width_mm = x * get_monitor_physical_size()[0]
        height_mm = y * get_monitor_physical_size()[1]
        return width_mm, height_mm
    
    # For all other units, use the JSON data for conversion
    for key, value in conversion_data.items():
        if value['reference'] == unit:
            conversion_equation = value['conversion_equation']
            break
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    
    # Evaluate the conversion equation
    width_mm = eval(conversion_equation.replace('x', str(x)))
    height_mm = eval(conversion_equation.replace('x', str(y)))
    
    return width_mm, height_mm

def convert_millimeters_to_pixels(width_mm, height_mm):
    """
    Convert the given dimensions in millimeters to pixels.
    
    :param width_mm: Width in millimeters.
    :param height_mm: Height in millimeters.
    :return: Tuple (width_px, height_px) representing the dimensions in pixels.
    """
    screen_width, screen_height = get_screen_resolution()
    width_mm_screen, height_mm_screen = get_monitor_physical_size()
    
    width_px = int(width_mm * (screen_width / width_mm_screen))
    height_px = int(height_mm * (screen_height / height_mm_screen))
    
    return width_px, height_px

def convert_from_pixels(width_px, height_px, output_unit, conversion_data):
    """
    Convert the given dimensions in pixels to the specified unit.
    
    :param width_px: Width in pixels.
    :param height_px: Height in pixels.
    :param output_unit: The unit to convert to (e.g., 'in', 'cm', 'mm', 'ratio', 'px').
    :param conversion_data: The dictionary containing the conversion equations.
    :return: Tuple (width, height) representing the dimensions in the desired unit.
    """
    screen_width, screen_height = get_screen_resolution()
    width_mm_screen, height_mm_screen = get_monitor_physical_size()
    
    # Convert pixels to millimeters first
    width_mm = width_px * (width_mm_screen / screen_width)
    height_mm = height_px * (height_mm_screen / screen_height)
    
    if output_unit == 'mm':
        return width_mm, height_mm
    elif output_unit == 'ratio':
        return width_px / screen_width, height_px / screen_height
    elif output_unit == 'px':
        return width_px, height_px
    else:
        # Use the JSON data to reverse the conversion
        for key, value in conversion_data.items():
            if value['reference'] == output_unit:
                conversion_equation = value['conversion_equation']
                break
        else:
            raise ValueError(f"Unsupported output unit: {output_unit}")
        
        # Reverse the conversion equation by dividing instead of multiplying
        reverse_equation = conversion_equation.replace('x', f'({width_mm})').replace('*', '/')
        width = eval(reverse_equation)
        
        reverse_equation = conversion_equation.replace('x', f'({height_mm})').replace('*', '/')
        height = eval(reverse_equation)
        
        return width, height

def calculate_window_size(x, y, unit, json_file='utils/conversion_data.json'):
    """
    Calculate the window size based on the input dimensions and unit.
    
    :param x: The width dimension.
    :param y: The height dimension.
    :param unit: The unit of measurement (e.g., 'in', 'cm', 'mm', 'ratio').
    :param json_file: Path to the JSON file containing conversion data.
    :return: Tuple (width, height) representing the window size in pixels.
    """
    conversion_data = load_conversion_data(json_file)
    width_mm, height_mm = convert_to_millimeters(x, y, unit, conversion_data)
    return convert_millimeters_to_pixels(width_mm, height_mm)
