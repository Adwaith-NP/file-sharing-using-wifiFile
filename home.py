import dearpygui.dearpygui as dpg
from local_home import home
from font_family.setUpFont import setup
from resizeSetUp import HomeResize,local_home_recize,loginResizer
from globalSharing.login import login
from globalSharing.signUp import signUp
from globalSharing.global_home import gl_home
    
def is_local_home_not_loaded():
    if dpg.does_item_exist("main_window"):
        dpg.hide_item("main_home_window")
        dpg.show_item("main_window")
        local_home_recize()
        dpg.set_viewport_resize_callback(lambda:local_home_recize())
    else:
        dpg.hide_item("main_home_window")
        home()
        
def is_auth():
    if dpg.does_item_exist("login_window"):
        dpg.hide_item("main_home_window")
        dpg.show_item("login_window")
        loginResizer()
        dpg.set_viewport_resize_callback(lambda:loginResizer())
    else:
        dpg.hide_item("main_home_window")
        login()
    

def main_home():
    if not dpg.does_item_exist("main_home_window"):
        with dpg.window(tag="main_home_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("ZENDER",tag="swname",pos=(0,0))
            dpg.add_button(label="local", tag="local_button", pos=(0, 0), width=120, height=40,callback=is_local_home_not_loaded)
            dpg.add_button(label="global", tag="globel_button", pos=(0, 0), width=120, height=40,callback=is_auth)

            # Customize button styles
            with dpg.theme(tag="button_theme"):
                with dpg.theme_component(dpg.mvButton):
                    dpg.add_theme_color(dpg.mvThemeCol_Button, (66, 100, 250, 255))  # Background color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (66, 150, 250, 180))  # Hover color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (66, 150, 250, 255))  # Active color
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))  # Text color
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)  # Rounded corners
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)  # Padding
                    
            with dpg.theme(tag="input_theme"):
                with dpg.theme_component(dpg.mvInputText):
                    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (30, 30, 30))   # Background color
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))    # Text color
                    dpg.add_theme_color(dpg.mvThemeCol_Border, (100, 100, 100))  # Border color
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)         # Rounded corners
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)
                    
                    
            
            
            dpg.bind_item_theme("local_button", "button_theme")
            dpg.bind_item_theme("globel_button", "button_theme")
            dpg.bind_item_font("swname",setup())
    HomeResize()
    dpg.set_viewport_resize_callback(lambda: HomeResize())
    
if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title='ZENDER file transfer', width=850, height=600)
    dpg.setup_dearpygui()

    main_home()

    dpg.show_viewport()
    dpg.start_dearpygui()

    dpg.destroy_context()