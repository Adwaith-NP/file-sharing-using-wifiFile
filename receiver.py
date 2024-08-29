import subprocess
import dearpygui.dearpygui as dpg
import threading
import socket
from subpart import get_downloas_dir,getIP,resize_and_update_buttons

stop_receiver = False

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
                download_directory = get_downloas_dir()
                file_name = download_directory / file_name
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
            except Exception as e:
                print(e)
                dpg.set_value("notifier", " An error occurred")
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
    