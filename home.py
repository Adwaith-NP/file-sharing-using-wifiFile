import dearpygui.dearpygui as dpg


from receiver import reciver_thred,receive_file
from sender import send_file
from subpart import resize_and_update_buttons



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
                    dpg.add_theme_color(dpg.mvThemeCol_Button, (66, 100, 250, 255))  # Background color
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