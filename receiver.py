import dearpygui.dearpygui as dpg
import threading
import socket
from subpart import get_downloas_dir,getIP
from resizeSetUp import local_home_recize,recevierResize
from font_family.setUpFont import setup

stop_receiver = False
local_ip = '120.0.0.1'

def activate():
    global stop_receiver
    stop_receiver = False

def receiver(host, port):
        global stop_receiver
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        
        
        while not stop_receiver:
            try:
                monitor()
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
                    server_socket.settimeout(20) ## new added chekit out
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
        return

def reciver_thred():
    host = '0.0.0.0'
    port = 12345
    threading.Thread(target=receiver, args=(host, port)).start()

def monitor():
    ip = getIP()
    if not ip or ip == local_ip:
        is_connection_established()

def is_connection_established():
    ip = getIP()
    global stop_receiver
    if ip and ip != local_ip:
        dpg.set_value("ip_address",f"Code : {ip.split('.')[-1]}")
        dpg.hide_item("refresh")
        stop_receiver = False
        reciver_thred()
    else:
        dpg.set_value("ip_address","Connection not established")
        dpg.show_item("refresh")
        stop_receiver = True
        

## receive page settings
def receive_file():
    def show_main_window():
        global stop_receiver
        stop_receiver = True
        dpg.hide_item("resive_window")
        dpg.show_item("main_window")
        local_home_recize()
        dpg.set_viewport_resize_callback(lambda: local_home_recize())
        
        
    if not dpg.does_item_exist("resive_window"):
        with dpg.window(tag="resive_window", label="Receive your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("", wrap=280, tag="ip_address", pos=(20, 80))
            dpg.add_button(label="Back", tag="back_button", pos=(20, 20), width=120, height=40 ,callback=show_main_window) 
            dpg.add_button(label="Refresh", tag="refresh", pos=(300,75), width=120, height=40 ,callback=is_connection_established) 
            dpg.add_text("connect and refresh...", wrap=280, tag="notifier", pos=(0, 0))
            dpg.bind_item_theme("back_button", "button_theme")
            dpg.bind_item_theme("refresh", "button_theme")
            dpg.bind_item_font("ip_address",setup("M"))
            dpg.bind_item_font("notifier",setup("M"))
            
            dpg.add_text("",tag="ip_of_sender")
            dpg.add_text("",tag="download_info")
    
    ip = getIP()
    if not ip or ip == local_ip:
        dpg.set_value("ip_address","Connection not established")
    else:
        dpg.set_value("ip_address",f"Code : {ip.split('.')[-1]}")
        dpg.hide_item("refresh")
        
            
              
        
    recevierResize()
    dpg.set_viewport_resize_callback(lambda: recevierResize())
    dpg.show_item("resive_window")
    dpg.hide_item("main_window")
    dpg.hide_item("ip_of_sender")
    dpg.hide_item("download_info")
    
    if ip and ip != local_ip:
        reciver_thred()
    