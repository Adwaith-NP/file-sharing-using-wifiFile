import dearpygui.dearpygui as dpg
import subprocess
import threading
import socket
import os
import time
import platform



stop_receiver = False
stop_searching = False

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


def receiver(host, port):
        global stop_receiver
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        

        while not stop_receiver:
            try:
                dpg.hide_item("ip_of_sender")
                dpg.hide_item("download_info")
                dpg.show_item("notifier")
                dpg.set_value("notifier", "Listening for connection...")
                server_socket.settimeout(1.0)  # Timeout to periodically check the stop flag
                client_socket, addr = server_socket.accept()
                
                dpg.set_value("notifier", "Connection established")
                
                file_name_length = int.from_bytes(client_socket.recv(4), 'big')  # Receive filename length
                file_name = client_socket.recv(file_name_length).decode('utf-8')
                file_name = "downloads/"+file_name
                file_size = int.from_bytes(client_socket.recv(8),'big')
                update_intervel = 1024 * 1024
                received_byts = 0
                file_size = int(file_size/update_intervel)
                
                dpg.hide_item("notifier")
                dpg.show_item("ip_of_sender")
                dpg.show_item("download_info")
                dpg.set_value("ip_of_sender",f"IP : {addr[0]}")
                
                
                with open(file_name, 'wb') as file:
                    while not stop_receiver:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        file.write(data)
                        received_byts += len(data)
                        dpg.set_value("download_info",f"downloading : {int(received_byts/update_intervel)}/{file_size}Mb")
                
                client_socket.close()
                dpg.hide_item("ip_of_sender")
                dpg.hide_item("download_info")
                dpg.show_item("notifier")
                dpg.set_value("notifier", f"File {file_name} download complited")
            except socket.timeout:
                continue
            except Exception:
                dpg.set_value("notifier", " An error occurred, restart the")
                break
        server_socket.close()

def reciver_thred():
    host = '0.0.0.0'
    port = 12345 
    threading.Thread(target=receiver, args=(host, port)).start()


## receive page settings
def receive_file():
    def show_main_window():
        global stop_receiver
        stop_receiver = True
        dpg.hide_item("resive_window")
        dpg.show_item("main_window")
        resize_and_update_buttons()
        dpg.set_viewport_resize_callback(lambda: resize_and_update_buttons())
        
        
        
    def resize():
        width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
        dpg.set_item_width("resive_window", width)
        dpg.set_item_height("resive_window", height)
        dpg.set_item_pos("notifier", [(width / 2) - 80, (height / 2) - 40])
        
        dpg.set_item_pos("ip_of_sender", [(width / 2) - 80, (height / 2) - 40])
        dpg.set_item_pos("download_info", [(width / 2) - 80, (height / 2)-20])
        
        
    if not dpg.does_item_exist("resive_window"):
        with dpg.window(tag="resive_window", label="Receive your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            ip = getIP()
            if not ip:
                dpg.add_text("Connect to a wifi and restart the application", wrap=280, tag="ip_address", pos=(20, 80))
            else:
                dpg.add_text(f"Your IP: {ip}", wrap=280, tag="ip_address", pos=(20, 80))
            dpg.add_button(label="Back", tag="back_button", pos=(20, 20), width=120, height=40 ,callback=show_main_window)
            dpg.add_text("connect and restart...", wrap=280, tag="notifier", pos=(0, 0))
            dpg.bind_item_theme("back_button", "button_theme")
            
            dpg.add_text("",tag="ip_of_sender")
            dpg.add_text("",tag="download_info")
            
              
        
    resize()
    dpg.set_viewport_resize_callback(lambda: resize())
    dpg.show_item("resive_window")
    dpg.hide_item("main_window")
    dpg.hide_item("ip_of_sender")
    dpg.hide_item("download_info")
    
    
    reciver_thred()
    
    
        
## send page settings
def send_file():
    
    def show_items():
        dpg.show_item("back_to_main")
        dpg.show_item("sed_button")
        dpg.hide_item("stop_button")
        dpg.hide_item("upload_info")
        global stop_searching
        stop_searching = False
    
    def stop_uploading_of_serching():
        global stop_searching
        stop_searching = True
        time.sleep(1.5)
        show_items()
    
    def show_main_window_for_send():
        dpg.hide_item("send_window")
        dpg.show_item("main_window")
        resize_and_update_buttons()
        dpg.set_viewport_resize_callback(lambda: resize_and_update_buttons())
    
    def sender(server_host,server_port,file_path):
        global stop_searching
        try:
            # Validate IP address format
            socket.inet_aton(server_host)
        except socket.error:
            dpg.set_value("warning","Warning : Invalid IP address format")
            show_items()
            return

        try:
            # Check if file exists
            if not os.path.isfile(file_path):
                dpg.set_value("warning","Warning : File not found")
                show_items()
                return
            
            dpg.set_value("warning","waiting for the connection")
            while not stop_searching :
                try:
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.settimeout(1.0)
                    client_socket.connect((server_host, server_port))
                except socket.error:
                    continue
                
                dpg.set_value("warning","")
                
                file_size_in_bytes = os.path.getsize(file_path)
                
                file_name = os.path.basename(file_path)
                file_name_bytes = file_name.encode('utf-8')
                file_name_length = len(file_name_bytes)
                
                client_socket.send(file_name_length.to_bytes(4, 'big'))
                client_socket.send(file_name_bytes)
                client_socket.send(file_size_in_bytes.to_bytes(8,'big'))

                sended_byte = 0
                update_interval = 1024 * 1024
                file_size_in_bytes  = int(file_size_in_bytes/update_interval)
                with open(file_path, 'rb') as file:
                    data = file.read(1024)
                    while data:
                        client_socket.send(data)
                        sended_byte += len(data)
                        data = file.read(1024)
                        if stop_searching:
                            dpg.set_value("warning","Warning : uploading stoped")
                            return
                        if sended_byte % update_interval == 0:
                            data_sended = sended_byte/update_interval
                            dpg.set_value("upload_info",f"file sending : {data_sended}/{file_size_in_bytes}Mb")
                client_socket.close()
                dpg.set_value("warning","File sent successfully")
                show_items()
                return 
            else:
                dpg.set_value("warning","Warning : stoped")
                show_items()
                return
        except:
            dpg.set_value("warning","Warning : error occurred retry")
            show_items()
            return
    
    def file_selection_fun():
        result = subprocess.run(['python3', 'file_selection.py'], capture_output=True, text=True)
        if result.returncode == 0:
            stdout_output = result.stdout.strip()
            dpg.set_value("path_text", stdout_output) 
            
    def send():
        ip_value = dpg.get_value("ip_input")
        port = 12345
        path_value = dpg.get_value("path_text")
        if ip_value == "":
            dpg.set_value("warning","Warning : Add IP")
        elif path_value == "             choos a file":
            dpg.set_value("warning","Warning : Add a file")
        else:
            dpg.hide_item("sed_button")
            dpg.hide_item("back_to_main")
            dpg.show_item("stop_button")
            dpg.show_item("upload_info")
            threading.Thread(target=sender, args=(ip_value, port,path_value)).start()
        
    def resize():
        width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
        dpg.set_item_width("send_window", width)
        dpg.set_item_height("send_window", height)
        dpg.set_item_pos("upload_info",[(width/2)-70, (height / 2)-100])
        dpg.set_item_pos("ip_text", [(width/2)-210, (height / 2) - 40])
        dpg.set_item_pos("ip_input", [(width/2)-60, (height / 2) - 40])
        dpg.set_item_pos("file_path",[(width/2)-210, (height / 2) + 10])
        dpg.set_item_pos("brows_file",[(width/2)+110, (height / 2) + 10])
        dpg.set_item_pos("sed_button",[(width/2)-210, (height / 2) + 60])
        
    if not dpg.does_item_exist("send_window"):
        with dpg.window(tag="send_window",label="send the file",pos=(0,0),no_title_bar=True,no_resize=True,no_move=True):
            dpg.add_text("",tag="warning",pos=(25,90))
            dpg.add_text("",tag="upload_info")
            dpg.add_button(label="back",tag="back_to_main",width=120, height=40,pos=(20, 20),callback=show_main_window_for_send)
            dpg.add_button(label="stop",tag="stop_button",width=120, height=40,pos=(20, 20),callback=stop_uploading_of_serching)
            dpg.add_text("enter ip of receiver",tag="ip_text",pos=(20,60))
            dpg.add_input_text(tag="ip_input",pos=(80,60),width=290)
            dpg.add_button(label="send",tag="sed_button",width=440, height=40,callback=send)
            dpg.add_button(label="Brows",tag="brows_file",width=120, height=35,callback=file_selection_fun)
            dpg.bind_item_theme("back_to_main", "button_theme")
            dpg.bind_item_theme("sed_button", "button_theme")
            dpg.bind_item_theme("brows_file", "button_theme")
            dpg.bind_item_theme("stop_button", "button_theme")
            with dpg.child_window(tag="file_path",pos=(0,0),width=300,height=35):
                dpg.add_text("             choos a file",tag="path_text")
        resize()
        dpg.set_viewport_resize_callback(lambda: resize())
        dpg.show_item("send_window")
        dpg.hide_item("main_window")
        dpg.hide_item("stop_button")

## main page settings

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

def home():
    if not dpg.does_item_exist("main_window"):
        with dpg.window(tag="main_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_button(label="Send", tag="sender_button", pos=(0, 0), width=120, height=40,callback=call_or_not_send)
            dpg.add_button(label="Receive", tag="receiver_button", pos=(0, 0), width=120, height=40, callback=call_or_not)

            # Customize button styles
            with dpg.theme(tag="button_theme"):
                with dpg.theme_component(dpg.mvButton):
                    dpg.add_theme_color(dpg.mvThemeCol_Button, (66, 150, 250, 255))  # Background color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (66, 150, 250, 180))  # Hover color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (66, 150, 250, 255))  # Active color
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))  # Text color
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)  # Rounded corners
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)  # Padding

            dpg.bind_item_theme("sender_button", "button_theme")
            dpg.bind_item_theme("receiver_button", "button_theme")

    resize_and_update_buttons()
    dpg.set_viewport_resize_callback(lambda: resize_and_update_buttons())

if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title='Appukuttan file transfer', width=800, height=600)
    dpg.setup_dearpygui()

    home()

    dpg.show_viewport()
    dpg.start_dearpygui()

    dpg.destroy_context()