import dearpygui.dearpygui as dpg
from receiver import reciver_thred,receive_file
from sender import send_file
from subpart import resize_and_update_buttons
from font_family.setUpFont import setup



def call_or_not():
    global stop_receiver
    if dpg.does_item_exist("resive_window"):
        stop_receiver = False
        reciver_thred()
        dpg.show_item("resive_window")
    else:
        dpg.hide_item("main_window")
        receive_file()

def call_or_not_send():
    if dpg.does_item_exist("send_window"):
        dpg.show_item("send_window")
    else:
        dpg.hide_item("main_window")
        send_file()
        
def to_mian_home():
    dpg.hide_item("main_window")
    dpg.show_item("main_home_window")
    
def text_recize():
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    dpg.set_item_pos("local_heading", [(width / 2)-100, (height / 2) - 180])

def home():
    if not dpg.does_item_exist("main_window"):
        with dpg.window(tag="main_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("Local File Transfer",pos=(0,0),tag="local_heading")
            dpg.add_button(label="Send", tag="sender_button", pos=(0, 0), width=120, height=40,callback=call_or_not_send)
            dpg.add_button(label="Receive", tag="receiver_button", pos=(0, 0), width=120, height=40, callback=call_or_not)
            dpg.add_button(label="Back",tag="back_to_main_home",width=120, height=40,pos=(20, 20),callback=to_mian_home)
            
        
            

            dpg.bind_item_theme("sender_button", "button_theme")
            dpg.bind_item_theme("receiver_button", "button_theme")
            dpg.bind_item_theme("back_to_main_home", "button_theme")
            dpg.bind_item_font("local_heading",setup())

    resize_and_update_buttons()
    text_recize()
    dpg.set_viewport_resize_callback(lambda: resize_and_update_buttons())
    dpg.set_viewport_resize_callback(lambda: text_recize())

# if __name__ == "__main__":
#     dpg.create_context()
#     dpg.create_viewport(title='Appukuttan file transfer', width=800, height=600)
#     dpg.setup_dearpygui()

#     home()

#     dpg.show_viewport()
#     dpg.start_dearpygui()

#     dpg.destroy_context()