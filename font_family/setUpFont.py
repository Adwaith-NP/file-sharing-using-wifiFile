from subpart import base_dir
import os
import dearpygui.dearpygui as dpg

arial_font = None

def setup():
    with dpg.font_registry():
        global arial_font
        if arial_font is None:
            # Add Arial font, adjust the size as needed (e.g., size=30)
            arial_font = dpg.add_font(os.path.join(base_dir(),"font_family/Arial.ttf"), size=30)
        return arial_font