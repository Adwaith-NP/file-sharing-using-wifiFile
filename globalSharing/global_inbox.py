import dearpygui.dearpygui as dpg
from font_family.setUpFont import setup
from resizeSetUp import globel_inbox_recize,globel_home_recize
data = [
    ["send","Adwaith"],
    ["Received","jalal"],
    ["Received","sreelal"],
    ["send","Sangeeth"],
    ["Received","Hashir"],
    ["send","Praveen"],
    ["send","Adharve"],
]

def back_to_home():
    dpg.hide_item("gl_inbox_window")
    dpg.show_item("main_gl_window")
    globel_home_recize()
    dpg.set_viewport_resize_callback(lambda:globel_home_recize())

def gl_inbox():
    if not dpg.does_item_exist("gl_inbox_window"):
        with dpg.window(tag="gl_inbox_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_button(label="Back",tag="gl_in_back_to_main_home",width=120, height=40,pos=(20, 20),callback=back_to_home)
            dpg.add_text("INBOX",tag="inbot_txt")
            dpg.add_button(label="sent",tag="inbox_sd_bt",width=100,height=40)
            dpg.add_button(label="received",tag="inbox_sd_re",width=100,height=40)
            with dpg.theme() as red_theme:
                with dpg.theme_component(dpg.mvText):
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0))
            with dpg.theme() as green_theme:
                with dpg.theme_component(dpg.mvText):
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 0))
            temp = 0
            with dpg.child_window(border=False,autosize_x=False,autosize_y=True,width=800,tag="ibox_child_window",no_scrollbar=True):
                for info in data:
                    ##Sent
                    if info[0] == "send":
                        with dpg.child_window(tag=f"gl_sd_file_path{temp}",pos=(20,temp),width=740,height=50):
                            dpg.add_text(f"Sent",tag=f"send_text{temp}",pos=(30,15))
                            dpg.add_text(f"Username : {info[1]}",tag=f"username{temp}",pos=(110,15))
                            dpg.add_text(f"File Name : exaple.exe",tag=f"file_name{temp}",pos=(280,15))
                            dpg.add_text(f"Time : 18/04/2004",tag=f"time{temp}",pos=(500,15))
                            dpg.add_text(f"Not seen",tag=f"status{temp}",pos=(650,15))
                            
                        dpg.bind_item_font(f"send_text{temp}",setup("S"))
                        dpg.bind_item_theme(f"send_text{temp}", red_theme)
                        dpg.bind_item_font(f"username{temp}",setup("S"))
                        dpg.bind_item_font(f"file_name{temp}",setup("S"))
                        dpg.bind_item_font(f"time{temp}",setup("S"))
                        dpg.bind_item_font(f"status{temp}",setup("S"))
                    else:
                    ##Receive
                        with dpg.child_window(tag=f"gl_re_file_path{temp}",pos=(20,temp),width=740,height=50):
                            dpg.add_text(f"Received",tag=f"send_text{temp}",pos=(30,15))
                            dpg.add_text(f"Username : {info[1]}",tag=f"username{temp}",pos=(110,15))
                            dpg.add_text(f"File Name : exaple.exe",tag=f"file_name{temp}",pos=(280,15))
                            dpg.add_text(f"Time : 18/04/2004",tag=f"time{temp}",pos=(500,15))
                            dpg.add_button(tag=f"download_bt{temp}",label="Download",width=80, height=30,pos=(650, 10))
                        dpg.bind_item_theme(f"download_bt{temp}", "button_theme")
                        dpg.bind_item_font(f"send_text{temp}",setup("S"))
                        dpg.bind_item_theme(f"send_text{temp}", green_theme)
                        dpg.bind_item_font(f"username{temp}",setup("S"))
                        dpg.bind_item_font(f"file_name{temp}",setup("S"))
                        dpg.bind_item_font(f"time{temp}",setup("S"))
                    temp += 60
                    
            
            dpg.bind_item_font("inbot_txt",setup("L"))
            dpg.bind_item_font("inbox_sd_bt",setup("S"))
            dpg.bind_item_font("inbox_sd_re",setup("S"))
            dpg.bind_item_theme("gl_in_back_to_main_home", "button_theme")
            dpg.bind_item_theme("inbox_sd_bt", "button_theme")
            dpg.bind_item_theme("inbox_sd_re", "button_theme")
        
    globel_inbox_recize()
    dpg.set_viewport_resize_callback(lambda: globel_inbox_recize())