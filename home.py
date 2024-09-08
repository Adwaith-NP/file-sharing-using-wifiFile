import dearpygui.dearpygui as dpg
from local_home import home
from font_family.setUpFont import setup

def resize():
    # Get the current viewport width and height
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    
    # Resize the window to match the viewport size
    dpg.set_item_width("main_home_window", width)
    dpg.set_item_height("main_home_window", height)
    
    # Update button positions
    dpg.set_item_pos("local_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("globel_button", [(width / 2) - 60, (height / 2) + 20])
    dpg.set_item_pos("swname", [(width / 2)-60, (height / 2) - 180])
    
def is_local_home_not_loaded():
    if dpg.does_item_exist("main_window"):
        dpg.hide_item("main_home_window")
        dpg.show_item("main_window")
    else:
        dpg.hide_item("main_home_window")
        home()
    

def main_home():
    if not dpg.does_item_exist("main_home_window"):
        with dpg.window(tag="main_home_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("ZENDER",tag="swname",pos=(0,0))
            dpg.add_button(label="local", tag="local_button", pos=(0, 0), width=120, height=40,callback=is_local_home_not_loaded)
            dpg.add_button(label="globel", tag="globel_button", pos=(0, 0), width=120, height=40)

            # Customize button styles
            with dpg.theme(tag="button_theme"):
                with dpg.theme_component(dpg.mvButton):
                    dpg.add_theme_color(dpg.mvThemeCol_Button, (66, 100, 250, 255))  # Background color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (66, 150, 250, 180))  # Hover color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (66, 150, 250, 255))  # Active color
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))  # Text color
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)  # Rounded corners
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)  # Padding
                    
            
            
            dpg.bind_item_theme("local_button", "button_theme")
            dpg.bind_item_theme("globel_button", "button_theme")
            dpg.bind_item_font("swname",setup())
    resize()
    dpg.set_viewport_resize_callback(lambda: resize())
    
if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title='ZENDER file transfer', width=800, height=600)
    dpg.setup_dearpygui()

    main_home()

    dpg.show_viewport()
    dpg.start_dearpygui()

    dpg.destroy_context()