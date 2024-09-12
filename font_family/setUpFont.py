from subpart import base_dir
import os
import dearpygui.dearpygui as dpg

arial_font_large = None
arial_font_size_mediom = None
arial_font_size_small = None

def setup(size = "L"):
    with dpg.font_registry():
        global arial_font_large
        global arial_font_size_mediom
        global arial_font_size_small
        if arial_font_large is None:
            arial_font_large = dpg.add_font(os.path.join(base_dir(),"font_family/Arial.ttf"), size=30)
            arial_font_size_mediom = dpg.add_font(os.path.join(base_dir(),"font_family/Arial.ttf"), size=24)
            arial_font_size_small = dpg.add_font(os.path.join(base_dir(),"font_family/Arial.ttf"), size=18)
    if size == "L":
        return arial_font_large
    elif size == "M":
        return arial_font_size_mediom
    return arial_font_size_small
            