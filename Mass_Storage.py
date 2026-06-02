from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

KV = '''
<Mass_Storage_Screen>:
    name: "mass_storage"

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Mass Storage'
            left_action_items: [["arrow-left", lambda x: app.change_screen("dashboard")]]

        # MAIN CONTENT
        MDBoxLayout:
            orientation: "horizontal"

            # --------------------------
            # NAVIGATION DOCK (20%)
            # --------------------------

            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: 0.2
                padding: dp(15)
                spacing: dp(15)
                md_bg_color: 0.15, 0.15, 0.15, 1

                MDLabel:
                    text: "Algorithms"             #TITLE NG NAV DOCK
                    halign: "center"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRaisedButton:
                    text: 'FCFS'                   #FCFS button
                    size_hint_x: 1
                    on_release:
                        root.fcfs_pressed()

                MDRaisedButton:                    #SSTF button
                    text: 'SSTF'
                    size_hint_x: 1
                    on_release:
                        root.sstf_pressed()

                MDRaisedButton:                     #SCAN button
                    text: 'SCAN'
                    size_hint_x: 1
                    on_release:
                        root.scan_pressed()

                MDRaisedButton:                     #C-SCAN button
                    text: 'C-SCAN'
                    size_hint_x: 1
                    on_release:
                        root.cscan_pressed()

                MDRaisedButton:
                    text: 'LOOK'             #LOOK button
                    size_hint_x: 1
                    on_release:
                        root.look_pressed()
                
                Widget:

            # --------------------------
            # MAIN CONTENT (80%)
            # --------------------------


            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: 0.8
                padding: dp(20)
                spacing: dp(20)

                # ==========================
                # INPUT SECTION
                # ==========================

                MDCard:
                    orientation: "vertical"
                    padding: dp(15)
                    spacing: dp(15)
                    radius: [15,15,15,15]
                    elevation: 3

                    MDLabel:
                        text: "Disk Scheduling Input"
                        halign: "center"
                        font_style: "H6"

                    MDGridLayout:
                        spacing: dp(15)
                        adaptive_height: True

                        MDTextField:
                            hint_text: "Enter Disk Queue"
                            helper_text: "Example: 98,183,37,122"
                            helper_text_mode: "on_focus"
                            mode: "rectangle"

                    MDRaisedButton:
                        text: "Visualize"
                        pos_hint: {"center_x": .5}
                        size_hint_x: 0.3

                # ==========================
                # DISK VISUALIZATION
                # ==========================

                MDCard:
                    orientation: "vertical"
                    padding: dp(15)
                    spacing: dp(15)
                    radius: [15,15,15,15]
                    elevation: 3
                    size_hint_y: 0.8

                    MDLabel:
                        text: "Disk Queue Visualization"
                        halign: "center"
                        font_style: "H6"

                    # VISUALIZATION AREA
                    MDCard:
                        md_bg_color: 0.95, 0.95, 0.95, 1
                        radius: [10,10,10,10]
                        elevation: 1
                        padding: dp(10)
                        size_hint_y: 0.7

                        Widget:

                    # BOTTOM INFO BOXES
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(15)
                        size_hint_y: 0.1




            
'''

Builder.load_string(KV)


class Mass_Storage_Screen(MDScreen):

    def fcfs_pressed(self):
        print("FCFS Button Pressed")

    def sstf_pressed(self):
        print("SSTF Button Pressed")

    def scan_pressed(self):
        print("SCAN Button Pressed")

    def cscan_pressed(self):
        print("C-SCAN Button Pressed")

    def look_pressed(self):
        print("LOOK Button Pressed")
