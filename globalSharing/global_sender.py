import dearpygui.dearpygui as dpg
from font_family.setUpFont import setup
from resizeSetUp import globel_sender_recize,globel_home_recize

def back_to_global_home():
    dpg.hide_item("gl_send_window")
    dpg.show_item("main_gl_window")
    globel_home_recize()
    dpg.set_viewport_resize_callback(lambda:globel_home_recize())
    

def gl_sender():
    if not dpg.does_item_exist("gl_send_window"):
            with dpg.window(tag="gl_send_window",label="send the file",pos=(0,0),no_title_bar=True,no_resize=True,no_move=True):
                dpg.add_text("Global Sender",tag="gl_sender_")
                dpg.add_input_text(hint="Username",tag="username",width=440)
                dpg.add_input_text(hint="File info",tag="sd_filename",width=440)
                dpg.add_button(label="Browse",tag="gl_file_browse",width=120, height=35)
                dpg.add_button(label="Send",tag="gl_send_button",width=440, height=40)
                dpg.add_button(label="Back",tag="gl_sd_back_to_main_home",width=120, height=40,pos=(20, 20),callback=back_to_global_home)
                
                dpg.bind_item_theme("gl_file_browse", "button_theme")
                dpg.bind_item_theme("gl_send_button", "button_theme")
                dpg.bind_item_theme("gl_sd_back_to_main_home", "button_theme")
                
                
                dpg.bind_item_theme("sd_filename","input_theme")
                dpg.bind_item_font("sd_filename",setup("S"))
                dpg.bind_item_theme("username","input_theme")
                dpg.bind_item_font("username",setup("S"))
                dpg.bind_item_font("gl_sender_",setup("L"))
                
                with dpg.child_window(tag="gl_file_path",pos=(0,0),width=300,height=35):
                    dpg.add_text("             choose a file",tag="gl_path_text")
    globel_sender_recize()
    dpg.set_viewport_resize_callback(lambda: globel_sender_recize())