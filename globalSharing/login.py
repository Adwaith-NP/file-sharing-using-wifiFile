import dearpygui.dearpygui as dpg
from resizeSetUp import loginResizer,HomeResize
from font_family.setUpFont import setup
from .ZENDER_API_Manager.login_API import auth_user
from globalSharing.global_home import gl_home
import threading

def hide_text():
    dpg.configure_item("login_message", show=False)

def login_verify():
    enterd_username = dpg.get_value('username')
    enterd_password = dpg.get_value('password')
    if auth_user(enterd_username,enterd_password):
        dpg.hide_item('login_window')
        gl_home()
    else:
        dpg.configure_item("login_message", show=True)
        threading.Timer(5.0, hide_text).start()
        
def go_to_home():
    dpg.hide_item("login_window")
    dpg.show_item("main_home_window")
    HomeResize()
    dpg.set_viewport_resize_callback(lambda:HomeResize())

def login():
    if not dpg.does_item_exist("login_window"):
        with dpg.window(tag="login_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("Login",tag="loginTag",pos=(0,0))
            dpg.add_text("Invalid username or password",tag="login_message")
            dpg.add_input_text(tag="username",hint="Username",pos=(20,50),width=290)
            dpg.add_input_text(tag="password",hint="password",pos=(20,70),width=290)
            dpg.add_checkbox(label="Remember password",tag="remember",pos=(20,100))
            dpg.add_button(tag="lo_back",label="back",width=120, height=40,pos=(20, 20),callback=go_to_home)
            dpg.add_button(tag="loginButton",label="Login",width=290,height=40,callback=login_verify)
            dpg.add_text("Don't have an account?",tag="signUp_info")
            dpg.add_button(tag="signUpButton",label="Singup",width=95,height=40)
            
            dpg.bind_item_theme("username","input_theme")
            dpg.bind_item_theme("password","input_theme")
            dpg.bind_item_theme("lo_back", "button_theme")
            dpg.bind_item_theme("loginButton", "button_theme")
            dpg.bind_item_theme("signUpButton", "button_theme")
            dpg.bind_item_font("username",setup("S"))
            dpg.bind_item_font("password",setup("S"))
            dpg.bind_item_font("signUp_info",setup("S"))
            dpg.bind_item_font("remember",setup("S"))
            dpg.bind_item_font("login_message",setup("M"))
            dpg.bind_item_font("loginTag",setup("L"))
            
            with dpg.theme() as red_theme:
                with dpg.theme_component(dpg.mvText):
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0))
                    
            dpg.bind_item_theme("login_message", red_theme)
            dpg.configure_item("login_message", show=False)
        
            
    loginResizer()
    dpg.set_viewport_resize_callback(lambda: loginResizer())