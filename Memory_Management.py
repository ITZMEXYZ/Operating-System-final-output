from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

KV = '''
<Memory_Management_Screen>:
    name: "memory_management"

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Memory Management'
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
                    text: "Memory Management"             #TITLE NG NAV DOCK
                    halign: "center"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRaisedButton:
                    text: 'MFT'                   #MFT button
                    size_hint_x: 1
                    on_release:
                        root.mft_pressed()

                MDRaisedButton:                    #MVT button
                    text: 'MVT'
                    size_hint_x: 1
                    on_release:
                        root.mvt_pressed()

                MDRaisedButton:                     #paging button
                    text: 'Paging'
                    size_hint_x: 1
                    on_release:
                        root.paging_pressed()

                MDRaisedButton:
                    text: 'Segmentation'             #segmentation button
                    size_hint_x: 1
                    on_release:
                        root.segmentation_pressed()
                
                Widget:

            # --------------------------
            # MAIN CONTENT (80%)
            # --------------------------

            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: 0.8
                padding: dp(20)
                spacing: dp(20)

'''

Builder.load_string(KV)


class Memory_Management_Screen(MDScreen):

    def mvt_pressed(self):
        print("MVT Button Pressed")

    def mft_pressed(self):
        print("MFT Button Pressed")

    def paging_pressed(self):
        print("Paging Button Pressed")

    def segmentation_pressed(self):
        print("Segmentation Button Pressed")