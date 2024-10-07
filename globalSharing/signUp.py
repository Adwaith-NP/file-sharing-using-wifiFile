import dearpygui.dearpygui as dpg
from resizeSetUp import signupResizer
from font_family.setUpFont import setup

def signUp():
    if not dpg.does_item_exist("signup_window"):
        with dpg.window(tag="signup_window", label="Send your file", pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True):
            dpg.add_button(tag="su_back",label="back",width=120, height=40,pos=(20, 20))
            dpg.add_text("Signup",tag="signupText")
            dpg.add_input_text(hint="Email",tag="signup_email",width=290)
            dpg.add_input_text(hint="Create an username",tag="signup_username",width=290)
            dpg.add_input_text(hint="create a password",tag="signup_passwprd",width=290)
            dpg.add_input_text(hint="Confierm password",tag="c_password",width=290)
            dpg.add_checkbox(label="I Agree to Privacy Policy",tag="privacy_policy")
            dpg.add_button(label="SignUp",tag="signup_bt",width=290,height=40)
            dpg.add_text("Have an account?",tag="login_text")
            dpg.add_button(label="Login",tag="login_bt",width=95,height=40)
            
            dpg.bind_item_font("signup_email",setup("S"))
            dpg.bind_item_font("signup_username",setup("S"))
            dpg.bind_item_font("signup_passwprd",setup("S"))
            dpg.bind_item_font("c_password",setup("S"))
            dpg.bind_item_font("signupText",setup("L"))
            dpg.bind_item_font("privacy_policy",setup("S"))
            dpg.bind_item_font("login_text",setup("S"))
            
            dpg.bind_item_theme("signup_email","input_theme")
            dpg.bind_item_theme("signup_username","input_theme")
            dpg.bind_item_theme("signup_passwprd","input_theme")
            dpg.bind_item_theme("c_password","input_theme")
            dpg.bind_item_theme("back", "button_theme")
            dpg.bind_item_theme("signup_bt", "button_theme")
            dpg.bind_item_theme("login_bt", "button_theme")
        
            
    signupResizer()
    dpg.set_viewport_resize_callback(lambda: signupResizer())