import dearpygui.dearpygui as dpg
from resizeSetUp import loginResizer
from font_family.setUpFont import setup

def login():
    if not dpg.does_item_exist("login_window"):
        with dpg.window(tag="login_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_text("Login",tag="loginTag",pos=(0,0))
            dpg.add_input_text(tag="username",hint="Username",pos=(20,50),width=290)
            dpg.add_input_text(tag="password",hint="password",pos=(20,70),width=290)
            dpg.add_checkbox(label="Remember password",tag="remember",pos=(20,100))
            dpg.add_button(tag="lo_back",label="back",width=120, height=40,pos=(20, 20))
            dpg.add_button(tag="loginButton",label="Login",width=290,height=40)
            dpg.add_text("Don't have an account?",tag="signUp_info")
            dpg.add_button(tag="signUpButton",label="Singup",width=95,height=40)
            
            dpg.bind_item_theme("username","input_theme")
            dpg.bind_item_theme("password","input_theme")
            dpg.bind_item_theme("back", "button_theme")
            dpg.bind_item_theme("loginButton", "button_theme")
            dpg.bind_item_theme("signUpButton", "button_theme")
            dpg.bind_item_font("username",setup("S"))
            dpg.bind_item_font("password",setup("S"))
            dpg.bind_item_font("signUp_info",setup("S"))
            dpg.bind_item_font("remember",setup("S"))
            dpg.bind_item_font("loginTag",setup("L"))
        
            
    loginResizer()
    dpg.set_viewport_resize_callback(lambda: loginResizer())