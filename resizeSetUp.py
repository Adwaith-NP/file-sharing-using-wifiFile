import dearpygui.dearpygui as dpg

def HomeResize():
    # Get the current viewport width and height
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    
    # Resize the window to match the viewport size
    dpg.set_item_width("main_home_window", width)
    dpg.set_item_height("main_home_window", height)
    
    # Update button positions
    dpg.set_item_pos("local_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("globel_button", [(width / 2) - 60, (height / 2) + 20])
    dpg.set_item_pos("swname", [(width / 2)-60, (height / 2) - 180])
    
def local_home_recize():
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    
    # Resize the window to match the viewport size
    dpg.set_item_width("main_window", width)
    dpg.set_item_height("main_window", height)
    
    # Update button positions
    dpg.set_item_pos("sender_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("receiver_button", [(width / 2) - 60, (height / 2) + 20])
    dpg.set_item_pos("local_heading", [(width / 2)-100, (height / 2) - 180])
    

def Sender_resize():
        width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
        dpg.set_item_width("send_window", width)
        dpg.set_item_height("send_window", height)
        dpg.set_item_pos("upload_info",[(width/2)-70, (height / 2)-100])
        dpg.set_item_pos("ip_text", [(width/2)-210, (height / 2) - 40])
        dpg.set_item_pos("ip_input", [(width/2)-60, (height / 2) - 40])
        dpg.set_item_pos("file_path",[(width/2)-210, (height / 2) + 10])
        dpg.set_item_pos("brows_file",[(width/2)+110, (height / 2) + 10])
        dpg.set_item_pos("sed_button",[(width/2)-210, (height / 2) + 60])
        
def recevierResize():
        width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
        dpg.set_item_width("resive_window", width)
        dpg.set_item_height("resive_window", height)
        dpg.set_item_pos("notifier", [(width / 2) - 100, (height / 2) - 40])
        
        dpg.set_item_pos("ip_of_sender", [(width / 2) - 70, (height / 2) - 40])
        dpg.set_item_pos("download_info", [(width / 2) - 80, (height / 2)-20])