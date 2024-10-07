import subprocess
import dearpygui.dearpygui as dpg
import os
import time
import socket
import threading
from subpart import getIP
from resizeSetUp import local_home_recize,Sender_resize
from font_family.setUpFont import setup

stop_searching = False

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
        local_home_recize()
        dpg.set_viewport_resize_callback(lambda: local_home_recize())
    
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
                except socket.error as e:
                    print(e)
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
                    client_socket.settimeout(20)
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
        directory = os.path.dirname(os.path.abspath(__file__))
        file_selection_path = os.path.join(directory,'file_selection.py')
        result = subprocess.run(['python3', file_selection_path], capture_output=True, text=True)
        if result.returncode == 0:
            stdout_output = result.stdout.strip()
            dpg.set_value("path_text", stdout_output) 
            
    def send():
        device_ip = getIP()
        if device_ip:
            cut_ip = ".".join(device_ip.split('.')[:-1])+"."
        else:
            cut_ip = "" ## remove after debugging
        ip_value_in = dpg.get_value("ip_input")
        ip_value = cut_ip + ip_value_in
        port = 12345
        path_value = dpg.get_value("path_text")
        if ip_value_in == "":
            dpg.set_value("warning","Warning : Add IP")
        elif path_value == "             choos a file":
            dpg.set_value("warning","Warning : Add a file")
        else:
            dpg.hide_item("sed_button")
            dpg.hide_item("back_to_main")
            dpg.show_item("stop_button")
            dpg.show_item("upload_info")
            threading.Thread(target=sender, args=(ip_value, port,path_value)).start()
        
    if not dpg.does_item_exist("send_window"):
        with dpg.window(tag="send_window",label="send the file",pos=(0,0),no_title_bar=True,no_resize=True,no_move=True):
            dpg.add_text("",tag="warning",pos=(25,90))
            dpg.add_text("",tag="upload_info")
            dpg.add_button(label="back",tag="back_to_main",width=120, height=40,pos=(20, 20),callback=show_main_window_for_send)
            dpg.add_button(label="stop",tag="stop_button",width=120, height=40,pos=(20, 20),callback=stop_uploading_of_serching)
            dpg.add_text("Enter the code",tag="ip_text",pos=(20,60))
            dpg.add_input_text(tag="ip_input",pos=(80,60),width=290)
            dpg.add_button(label="send",tag="sed_button",width=440, height=40,callback=send)
            dpg.add_button(label="Browse",tag="brows_file",width=120, height=35,callback=file_selection_fun)
            dpg.bind_item_theme("back_to_main", "button_theme")
            dpg.bind_item_theme("sed_button", "button_theme")
            dpg.bind_item_theme("brows_file", "button_theme")
            dpg.bind_item_theme("stop_button", "button_theme")
            dpg.bind_item_font("ip_text",setup("S"))
                    
            dpg.bind_item_theme("ip_input","input_theme")
            dpg.bind_item_font("ip_input",setup("S"))
            
            with dpg.child_window(tag="file_path",pos=(0,0),width=300,height=35):
                dpg.add_text("             choose a file",tag="path_text")
        Sender_resize()
        dpg.set_viewport_resize_callback(lambda: Sender_resize())
        dpg.show_item("send_window")
        dpg.hide_item("main_window")
        dpg.hide_item("stop_button")
