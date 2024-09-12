import dearpygui.dearpygui as dpg
from receiver import reciver_thred,receive_file,activate
from sender import send_file
from font_family.setUpFont import setup
from resizeSetUp import local_home_recize,HomeResize,Sender_resize,recevierResize



def call_or_not():
    if dpg.does_item_exist("resive_window"):
        activate()
        reciver_thred()
        recevierResize()
        dpg.set_viewport_resize_callback(lambda:recevierResize())
        dpg.show_item("resive_window")
    else:
        dpg.hide_item("main_window")
        receive_file()

def call_or_not_send():
    if dpg.does_item_exist("send_window"):
        dpg.show_item("send_window")
        Sender_resize()
        dpg.set_viewport_resize_callback(lambda:Sender_resize())
    else:
        dpg.hide_item("main_window")
        send_file()
        
def to_mian_home():
    dpg.hide_item("main_window")
    dpg.show_item("main_home_window")
    HomeResize()
    dpg.set_viewport_resize_callback(lambda: HomeResize())
    

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

    local_home_recize()
    dpg.set_viewport_resize_callback(lambda: local_home_recize())