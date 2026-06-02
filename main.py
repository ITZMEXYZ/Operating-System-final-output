from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from CPU_Scheduling import CPU_Scheduling_Screen
from Memory_Management import Memory_Management_Screen
from Virtual_Memory import Virtual_Memory_Screen
from Mass_Storage import Mass_Storage_Screen


KV = '''
<DashboardScreen>:
    name: "dashboard"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "OS Visualizer Dashboard"
            subtitle: "GROUP 10"

        ScrollView:

            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(20)
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Operating System Visualizer"
                    halign: "center"
                    font_style: "H4"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRaisedButton:
                    text: "CPU Scheduling"
                    pos_hint: {"center_x": .5}
                    size_hint_x: 0.6
                    on_release:
                        app.change_screen("cpu_scheduling")

                MDRaisedButton:
                    text: "Memory Management"
                    pos_hint: {"center_x": .5}
                    size_hint_x: 0.6
                    on_release:
                        app.change_screen("memory_management")

                MDRaisedButton:
                    text: "Virtual Memory"
                    pos_hint: {"center_x": .5}
                    size_hint_x: 0.6
                    on_release:
                        app.change_screen("virtual_memory")

                MDRaisedButton:
                    text: "Mass Storage"
                    pos_hint: {"center_x": .5}
                    size_hint_x: 0.6
                    on_release:
                        app.change_screen("mass_storage")
'''

Builder.load_string(KV)


class DashboardScreen(MDScreen):
    pass


class MainApp(MDApp):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(DashboardScreen())
        sm.add_widget(CPU_Scheduling_Screen())
        sm.add_widget(Memory_Management_Screen())
        sm.add_widget(Virtual_Memory_Screen())
        sm.add_widget(Mass_Storage_Screen())

        return sm

    def change_screen(self, screen_name):
        self.root.current = screen_name


MainApp().run()