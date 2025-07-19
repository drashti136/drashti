from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.uix.image import Image  # For clothing icon
from kivymd.uix.dialog import MDDialog

class Clothing(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        # 👕 Add clothing image
        cloth_icon = Image(
            source="cloths.png",
            size_hint=(None, None),
            size=(120, 120),
            pos_hint={'center_x': 0.5, 'center_y': 0.75}
        )

        # Name Input Field
        self.name_input = MDTextField(
            hint_text="Enter your name",
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint_x=None,
            width=300,
            height="40dp"
        )

        # Contact Number Input Field
        self.contact_input = MDTextField(
            hint_text="Enter contact number",
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            size_hint_x=None,
            width=300,
            height="40dp"
        )

        # Change Contact No. Button (as clickable text)
        change_btn = MDFlatButton(
            text="Change Contact No.",
            font_size="12sp",
            theme_text_color="Custom",           # 👈 Required to customize color
            text_color=(0.6, 0.6, 0.6, 1), 
            pos_hint={'center_x': 0.5, 'center_y': 0.40},
            on_release=self.change_contact_action
        )

        # Start Button
        button = MDRectangleFlatButton(
            text='Start',
            pos_hint={'center_x': 0.5, 'center_y': 0.30},
            on_release=self.show_data
        )

        # Add all widgets
        screen.add_widget(cloth_icon)
        screen.add_widget(self.name_input)
        screen.add_widget(self.contact_input)
        screen.add_widget(change_btn)
        screen.add_widget(button)

        return screen

    def show_data(self, obj):
        name = self.name_input.text
        contact = self.contact_input.text
        print(f"Name: {name}")
        print(f"Contact: {contact}")

    def change_contact_action(self, obj):
        print("📝 'Change Contact No.' button clicked!")

        # Add inside the Clothing class:
    def show_data(self, obj):
        name = self.name_input.text.strip()
        contact = self.contact_input.text.strip()

        if not contact.isdigit() or len(contact) != 10:
            self.show_invalid_dialog("Please enter a valid 10-digit number.")
        elif not name:
            self.show_invalid_dialog("Please enter your name.")
        else:
            print(f"Name: {name}")
            print(f"Contact: {contact}")

            self.stop()
            import subprocess, sys
            python_exec = sys.executable
            subprocess.Popen([python_exec, "clothsapp.py"], shell=True)

    # Add this function in your Clothing class:
    def show_invalid_dialog(self, message):
        dialog = MDDialog(
            title="❌ Invalid Input",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

Clothing().run()

