import dearpygui.dearpygui as dpg
from font_family.setUpFont import setup
from resizeSetUp import globel_home_recize,HomeResize

def go_back_to_home():
    dpg.hide_item("main_gl_window")
    dpg.show_item("main_home_window")
    HomeResize()
    dpg.set_viewport_resize_callback(lambda:HomeResize())
    
def gl_home():
    if not dpg.does_item_exist("main_gl_window"):
        with dpg.window(tag="main_gl_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("Global File Transfer",pos=(0,0),tag="gb_local_heading")
            dpg.add_button(label="Send", tag="gb_sender_button", pos=(0, 0), width=120, height=40)
            dpg.add_button(label="Inbox", tag="gb_receiver_button", pos=(0, 0), width=120, height=40)
            dpg.add_button(label="Back",tag="gl_back_to_main_home",width=120, height=40,pos=(20, 20),callback=go_back_to_home)
            
            dpg.bind_item_theme("gb_sender_button", "button_theme")
            dpg.bind_item_theme("gb_receiver_button", "button_theme")
            dpg.bind_item_theme("gl_back_to_main_home", "button_theme")
            dpg.bind_item_font("gb_local_heading",setup())
    
    else:
        dpg.hide_item("main_home_window")
        dpg.show_item("main_gl_window")

    globel_home_recize()
    dpg.set_viewport_resize_callback(lambda: globel_home_recize())