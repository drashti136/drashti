from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.utils import platform
import webbrowser
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import json
from datetime import datetime, timedelta

KV = '''
MDNavigationLayout:

    ScreenManager:
        id: screen_manager

        MDScreen:
            name: "home"

            MDBoxLayout:
                orientation: 'vertical'

                MDTopAppBar:
                    title: 'Clothing Application'
                    elevation: 4
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["phone", lambda x: app.on_icon_tap('call')], ["whatsapp", lambda x: app.on_icon_tap('whatsapp')]]

                MDBoxLayout:
                    orientation: "horizontal"
                    pos_hint: {"center_y": 0.60} 
                    spacing: "10dp"
                    padding: "10dp", "0dp"
                    size_hint_y: None
                    height: self.minimum_height

                    MDIcon:
                        icon: "bell"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        size_hint_x: None
                        width: "50dp"

                    MDFlatButton:
                        text: "Notifications"
                        halign: "left"
                        on_release: app.on_icon_tap('notification')

                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: "40dp"
                    spacing: "5dp"
                    padding: "10dp", "0dp"

                    MDIcon:
                        icon: "arrow-right"
                        theme_text_color: "Custom"
                        text_color: 1, 0, 0, 1
                        size_hint_y: None
                        height: "24dp"

                    MDLabel:
                        text: "[color=FF0000]Hello Customer![/color]"
                        markup: True
                        halign: "left"
                        size_hint_y: None
                        height: "24dp"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        font_style: "Subtitle1"

                Widget:

                MDBoxLayout:
                    size_hint_y: None
                    height: "340dp"
                    padding: "10dp"

                    MDGridLayout:
                        cols: 2
                        spacing: "10dp"
                        padding: "10dp"
                        size_hint_y: None
                        height: self.minimum_height

                        Image:
                            source: "m1.jpeg"
                            size_hint: None, None
                            size: "150dp", "150dp"
                        Image:
                            source: "m2.jpeg"
                            size_hint: None, None
                            size: "150dp", "150dp"
                        Image:
                            source: "m3.jpeg"
                            size_hint: None, None
                            size: "150dp", "150dp"
                        Image:
                            source: "m4.jpeg"
                            size_hint: None, None
                            size: "150dp", "150dp"
        MDScreen:
            name: "cloths_info"
            MDTopAppBar:
                title: "About Clothes"
                elevation: 4
                pos_hint: {"top": 1}
                left_action_items: [['arrow-left', lambda x: app.change_screen("home")]]

            
            MDLabel:
                text: "🧥 Here is cloths information..."
                halign: "center"
                pos_hint: {"top": 0.88}
                size_hint_y: None
                height: self.texture_size[1]

            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "10dp"
                pos_hint: {"top": 0.85}
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "👉 we provide high-quality cloths with affordable prices.\\n👉 Serving customers since 2022.\\n👉 our cloths is branded"
                    halign: "left"
                    text_size: self.width, None
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

        MDScreen:
            name: "owner"
            MDTopAppBar:
                title: "Owner"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]

            MDLabel:
                text: "Owner Details Here"
                halign: "center"
                pos_hint: {"top": 0.88}
                size_hint_y: None
                height: self.texture_size[1]

            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "10dp"
                pos_hint: {"top": 0.85}
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Drahsti bhingradiya`s Clothing Brand"
                    halign: "left"
                    text_size: self.width, None
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]        

        MDScreen:
            name: "address"
            MDTopAppBar:
                title: "Address"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]

    
            MDLabel:
                text: "Address Details Here"
                halign: "center"
                pos_hint: {"top": 0.88}
                size_hint_y: None
                height: self.texture_size[1]

            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "10dp"
                pos_hint: {"top": 0.85}
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Surat,Gujrat"
                    halign: "left"
                    text_size: self.width, None
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]        
        
        MDScreen:
            name: "location"
            MDTopAppBar:
                title: "Location"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]

            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "20dp"
                pos_hint: {"top": 0.90}
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "📍 Visit Us:"
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextButton:
                    text: "🗺️ Open in Google Maps"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0, 0, 1, 1
                    on_release: app.open_map()

        MDScreen:
            name: "previous_messages"
            MDTopAppBar:
                title: "Previous Messages"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]
                
            MDLabel:
                text: "Our previous messages will appear here."
                halign: "center"
                pos_hint: {"top": 0.88}
                size_hint_y: None
                height: self.texture_size[1]

        MDScreen:
            name: "time"
            MDTopAppBar:
                title: "Time"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]
            
            MDLabel:
                text: "Time details here."
                halign: "center"
                pos_hint: {"top": 0.88}
                size_hint_y: None
                height: self.texture_size[1]

            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "10dp"
                pos_hint: {"top": 0.85}
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Monday to Saturday: 11 AM to 7 PM \\nSunday: 1 PM to 6 PM"
                    halign: "left"
                    text_size: self.width, None
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]
                
        MDScreen:
            name: "ask_us"
            MDTopAppBar:
                title: "Ask Us"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]

            MDBoxLayout:
                orientation: 'vertical'
                spacing: "10dp"
                padding: "20dp"

                MDLabel:
                    text: "Ask Us Anything!"
                    halign: "center"
                    pos_hint: {"top": 0.88}
                    size_hint_y: None
                    height: self.texture_size[1]
                
                MDTextField:
                    id: chat_input
                    hint_text: "Type your question here"
                    multiline: True

                MDRaisedButton:
                    text: "Send"
                    pos_hint: {"center_x": 0.5}
                    on_press:
                        app.send_message()

        MDScreen:
            name: "profile"
            MDTopAppBar:
                title: "Your Profile"
                pos_hint: {"top": 1}
                left_action_items: [["arrow-left", lambda x: app.change_screen("home")]]
            
            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "10dp"
                
                FloatLayout:
                    MDLabel:
                        text: "Change Your Number"
                        halign: "center"
                        pos_hint: {"top": 0.15}
                        size_hint_y: None
                        height: self.texture_size[1]     

                MDTextField:
                    id: phone_input
                    hint_text: "Enter new phone number"
                    input_filter: "int"
                    max_text_length: 10
                    mode: "rectangle"

                MDRaisedButton:
                    text: "Update Number"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.validate_phone_number()

    MDNavigationDrawer:
        id: nav_drawer
        radius: [0, 0, 0, 0]

        BoxLayout:
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"

            MDLabel:
                text: "Clothing"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]

            ScrollView:
                MDList:

                    OneLineIconListItem:
                        text: "About Us"
                        on_release:
                            app.change_screen("cloths_info")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "information"

                    OneLineIconListItem:
                        text: "Owner"
                        on_press:
                            app.change_screen("owner")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "account"

                    OneLineIconListItem:
                        text: "Address"
                        on_press:
                            app.change_screen("address")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "map-marker"

                    OneLineIconListItem:
                        text: "Location"
                        on_press:
                            app.change_screen("location")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "map"

                    OneLineIconListItem:
                        text: "Previous Messages"
                        on_press:
                            app.change_screen("previous_messages")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "message-reply-text"

                    OneLineIconListItem:
                        text: "Time"
                        on_press:
                            app.change_screen("time")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "clock-outline"

                    OneLineIconListItem:
                        text: "Ask Us"
                        on_press:
                            app.change_screen("ask_us")
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "chat-question"

            Widget:
                size_hint_y: None
                height: "20dp"

            MDSeparator:

            OneLineIconListItem:
                text: "Your Profile"
                on_press:
                    app.change_screen("profile")
                    nav_drawer.set_state("close")
                IconLeftWidget:
                    icon: "account-circle"
'''
class Clothing(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_icon_tap(self, icon_name):
        if icon_name == "whatsapp":
            self.open_whatsapp()
        elif icon_name == "call":
            self.make_call()
        else:
            print(f"🔘 {icon_name} icon tapped")

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def send_message(self):
        chat_input = self.root.ids.chat_input.text
        print(f"💬 Message sent: {chat_input}")
        self.root.ids.chat_input.text = ""

    def update_number(self):
        phone_input = self.root.ids.phone_input.text
        print(f"📱 New number: {phone_input}")
        self.root.ids.phone_input.text = ""

    def change_screen(self, name):
        self.root.ids.screen_manager.current = name

    def build(self):
        return Builder.load_string(KV)

    def open_map(self):
        # Use your actual location URL here
        url = "https://maps.app.goo.gl/M8BvVF7VacUM5vLS7"
        webbrowser.open(url)

    def open_whatsapp(self):
        # Full number: +91 9724855166 → Must be: 919724855166
        country_code = "91"
        phone_last_10_digits = "9724855166"
        message = "Hello"

        full_number = country_code + phone_last_10_digits
        message_encoded = message.replace(" ", "%20")

        url = f"https://wa.me/{full_number}?text={message_encoded}"
        webbrowser.open(url)

    def make_call(self):
        if platform == 'android':
            from jnius import autoclass, cast
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            phone_number = "tel:+919724855166"
            intent = Intent(Intent.ACTION_DIAL)
            intent.setData(Uri.parse(phone_number))

            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        else:
            print("⚠️ Call feature works only on Android.")

    dialog = None
    success_dialog = None

    def validate_phone_number(self):
        phone = self.root.ids.phone_input.text.strip()

        if not phone.isdigit() or len(phone) != 10:
            self.show_invalid_popup()
        else:
            self.show_success_popup()
            print("✅ Phone number updated:", phone)  # Replace with your update logic

    def show_invalid_popup(self):
        if self.invalid_dialog:
            self.invalid_dialog.dismiss()

        self.invalid_dialog = MDDialog(
            title="❌ Invalid Number",
            text="Please enter exactly 10 digits.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.invalid_dialog.dismiss()
                )
            ],
        )
        self.invalid_dialog.open()

    def show_success_popup(self):
        if self.success_dialog:
            self.success_dialog.dismiss()

        self.success_dialog = MDDialog(
            title="✅ Success",
            text="Your number has been updated successfully.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.success_dialog.dismiss()
                )
            ],
        )
        self.success_dialog.open()
  
          
Clothing().run()
