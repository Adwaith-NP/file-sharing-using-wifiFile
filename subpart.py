import platform
from pathlib import Path
import socket
import dearpygui.dearpygui as dpg



def get_downloas_dir():
    home_dir = Path.home()
    downloads_dir = home_dir / 'Downloads'
    return downloads_dir
def getIP():
    os_name = ""
    os_type = platform.system()
    if os_type == "Darwin":
        os_name = "macOS"
    elif os_type == "Windows":
        os_name =  "Windows"
    
    if os_name == "macOS":
        try:
            import netifaces ## installed
            # Get the appropriate interface names for the current OS
            interfaces = ['en0', 'en1']
            # Loop through all network interfaces
            for interface in netifaces.interfaces():
                if interface in interfaces:
                    # Get the addresses for the interface
                    addresses = netifaces.ifaddresses(interface)
                    # Check if there is an IPv4 address
                    if netifaces.AF_INET in addresses:
                        # Return the IP address
                        return addresses[netifaces.AF_INET][0]['addr']
            return False
        except :
            return False
    else :
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        if local_ip:
            return local_ip
        return False
    
def resize_and_update_buttons():
    # Get the current viewport width and height
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    
    # Resize the window to match the viewport size
    dpg.set_item_width("main_window", width)
    dpg.set_item_height("main_window", height)
    
    # Update button positions
    dpg.set_item_pos("sender_button", [(width / 2) - 60, (height / 2) - 40])
    dpg.set_item_pos("receiver_button", [(width / 2) - 60, (height / 2) + 20])