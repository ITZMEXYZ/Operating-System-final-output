from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


KV = '''
ScreenManager:
    DashboardScreen:
    CPUScreen:
    MemoryScreen:
    VirtualMemoryScreen:
    MassStorageScreen:


<DashboardScreen>:
    name: "dashboard"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "OS Visualizer Dashboard"

            ScrollView:

                MDBoxLayout:
                    orientation: "horizontal"
                    padding: dp(20)
                    spacing: dp(20)
                    adaptive_height: True

                    MDLabel:
                        text: "Operating System Visualizer"
                        halign: "center"
                        font_style: "H4"
                        adaptive_height: True

                    MDRaisedButton:
                        text: "CPU Scheduling"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("cpu")

                    MDRaisedButton:
                        text: "Memory Management"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("memory")

                    MDRaisedButton:
                        text: "Virtual Memory"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("virtual_memory")

                    MDRaisedButton:
                        text: "Mass Storage"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("mass_storage")


<CPUScreen>:
    name: "cpu"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "CPU Scheduling"
            left_action_items: [["arrow-left", lambda x: app.change_screen("dashboard")]]

        MDLabel:
            text: "CPU Scheduling Algorithms"
            halign: "center"


<MemoryScreen>:
    name: "memory"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Memory Management"
            left_action_items: [["arrow-left", lambda x: app.change_screen("dashboard")]]

        MDLabel:
            text: "Memory Management Algorithms"
            halign: "center"


<VirtualMemoryScreen>:
    name: "virtual_memory"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Virtual Memory"
            left_action_items: [["arrow-left", lambda x: app.change_screen("dashboard")]]

        MDLabel:
            text: "Virtual Memory Algorithms"
            halign: "center"


<MassStorageScreen>:
    name: "mass_storage"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Mass Storage"
            left_action_items: [["arrow-left", lambda x: app.change_screen("dashboard")]]

        MDLabel:
            text: "Disk Scheduling Algorithms"
            halign: "center"
'''


class DashboardScreen(Screen):
    pass


class CPUScreen(Screen):
    pass


class MemoryScreen(Screen):
    pass


class VirtualMemoryScreen(Screen):
    pass


class MassStorageScreen(Screen):
    pass


class DashboardApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name


DashboardApp().run()