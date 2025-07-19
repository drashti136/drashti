from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
import subprocess
import sys

class Clothing(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.dialog = None  # initialize dialog reference

        screen = Screen()

        cloth_icon = Image(
            source="cloths.png",
            size_hint=(None, None),
            size=(120, 120),
            pos_hint={'center_x': 0.5, 'center_y': 0.75}
        )

        self.name_input = MDTextField(
            hint_text="Enter your name",
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint_x=None,
            width=300,
            height="40dp"
        )

        self.contact_input = MDTextField(
            hint_text="Enter contact number",
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            size_hint_x=None,
            width=300,
            height="40dp"
        )

        button = MDRectangleFlatButton(
            text='Start',
            pos_hint={'center_x': 0.5, 'center_y': 0.30},
            on_release=self.show_data
        )

        screen.add_widget(cloth_icon)
        screen.add_widget(self.name_input)
        screen.add_widget(self.contact_input)
        screen.add_widget(button)

        return screen

    def show_data(self, obj):
        name = self.name_input.text.strip()
        contact = self.contact_input.text.strip()

        if not contact.isdigit() or len(contact) != 10:
            self.contact_input.text_color = (1, 0, 0, 1)  # red color
            self.show_invalid_dialog("Please enter a valid 10-digit number.")
        elif not name:
            self.show_invalid_dialog("Please enter your name.")
        else:
            print(f"Name: {name}")
            print(f"Contact: {contact}")
            self.stop()
            python_exec = sys.executable
            subprocess.Popen([python_exec, "clothing2.py"], shell=True)

    def show_invalid_dialog(self, message):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(
            title="❌ Invalid Input",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ],
        )
        self.dialog.open()


Clothing().run()
