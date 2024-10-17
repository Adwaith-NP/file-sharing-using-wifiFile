import dearpygui.dearpygui as dpg

def set_window_size(name):
    # Get the current viewport width and height
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    
    # Resize the window to match the viewport size
    dpg.set_item_width(name, width)
    dpg.set_item_height(name, height)
    return [width,height]

def HomeResize():
    size = set_window_size("main_home_window")
    width,height= size[0],size[1]
    # Update button positions
    dpg.set_item_pos("local_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("globel_button", [(width / 2) - 60, (height / 2) + 20])
    dpg.set_item_pos("swname", [(width / 2)-60, (height / 2) - 180])
    
def local_home_recize():
    size = set_window_size("main_window")
    width,height= size[0],size[1]
    
    # Update button positions
    dpg.set_item_pos("sender_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("receiver_button", [(width / 2) - 60, (height / 2) + 20])
    dpg.set_item_pos("local_heading", [(width / 2)-100, (height / 2) - 180])
    

def Sender_resize():
        size = set_window_size("send_window")
        width,height= size[0],size[1]
        dpg.set_item_pos("upload_info",[(width/2)-70, (height / 2)-100])
        dpg.set_item_pos("ip_text", [(width/2)-210, (height / 2) - 40])
        dpg.set_item_pos("ip_input", [(width/2)-60, (height / 2) - 40])
        dpg.set_item_pos("file_path",[(width/2)-210, (height / 2) + 10])
        dpg.set_item_pos("brows_file",[(width/2)+110, (height / 2) + 10])
        dpg.set_item_pos("sed_button",[(width/2)-210, (height / 2) + 60])
        
def recevierResize():
        size = set_window_size("resive_window")
        width,height= size[0],size[1]
        
        dpg.set_item_pos("notifier", [(width / 2) - 100, (height / 2) - 40])
        dpg.set_item_pos("ip_of_sender", [(width / 2) - 70, (height / 2) - 40])
        dpg.set_item_pos("download_info", [(width / 2) - 80, (height / 2)-20])
        
def loginResizer():
        size = set_window_size("login_window")
        width,height= size[0],size[1]
        
        dpg.set_item_pos("loginTag", [(width / 2) - 40, (height / 2) - 180])
        dpg.set_item_pos("login_message", [(width / 2) + 70, (height / 2) - 260])
        dpg.set_item_pos("username", [(width / 2) - 150, (height / 2) - 80])
        dpg.set_item_pos("password", [(width / 2) - 150, (height / 2) - 30])
        dpg.set_item_pos("remember", [(width / 2) - 150, (height / 2) + 20])
        dpg.set_item_pos("loginButton", [(width / 2) - 150, (height / 2) + 50])
        dpg.set_item_pos("signUp_info", [(width / 2) - 150, (height / 2) + 130])
        dpg.set_item_pos("signUpButton", [(width / 2) + 45, (height / 2) + 120])
        
def signupResizer():
        size = set_window_size("signup_window")
        width,height= size[0],size[1]
        
        dpg.set_item_pos("signupText", [(width / 2) - 55, (height / 2) - 250])
        dpg.set_item_pos("signup_email", [(width / 2) - 150, (height / 2) - 180])
        dpg.set_item_pos("signup_username", [(width / 2) - 150, (height / 2) - 130])
        dpg.set_item_pos("signup_passwprd", [(width / 2) - 150, (height / 2) - 80])
        dpg.set_item_pos("c_password", [(width / 2) - 150, (height / 2)-30])
        dpg.set_item_pos("privacy_policy", [(width / 2) - 150, (height / 2) + 20])
        dpg.set_item_pos("signup_bt", [(width / 2) - 150, (height / 2) + 60])
        dpg.set_item_pos("login_text", [(width / 2) - 150, (height / 2) + 140])
        dpg.set_item_pos("login_bt", [(width / 2) + 45, (height / 2) + 130])
        
        
def globel_home_recize():
    size = set_window_size("main_gl_window")
    width,height= size[0],size[1]
    
    # Update button positions
    dpg.set_item_pos("gb_sender_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("gb_receiver_button", [(width / 2) - 60, (height / 2) + 20])
    dpg.set_item_pos("gb_local_heading", [(width / 2)-110, (height / 2) - 180])
    
def globel_sender_recize():
    size = set_window_size("gl_send_window")
    width,height= size[0],size[1]
    dpg.set_item_pos("gl_sender_", [(width / 2) - 90, (height / 2) - 250])
    dpg.set_item_pos("gl_send_username", [(width/2)-210, (height / 2) - 40])
    dpg.set_item_pos("sd_filename", [(width/2)-210, (height / 2) + 10])
    dpg.set_item_pos("gl_file_path",[(width/2)-210, (height / 2) + 60])
    dpg.set_item_pos("gl_file_browse",[(width/2)+110, (height / 2) + 60])
    dpg.set_item_pos("gl_send_button",[(width/2)-210, (height / 2) + 110])
    
def globel_inbox_recize():
    size = set_window_size("gl_inbox_window")
    width,height= size[0],size[1]
    dpg.set_item_pos("inbot_txt", [(width / 2) - 40, (height / 2) - 250])
    dpg.set_item_pos("inbox_sd_bt", [(width / 2) + 30, (height / 2) - 150])
    dpg.set_item_pos("inbox_sd_re", [(width / 2) - 130, (height / 2) - 150])
    dpg.set_item_pos("ibox_child_window", [(width / 2) - 395, (height / 2) - 50])