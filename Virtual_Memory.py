from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

KV = '''
<Virtual_Memory_Screen>:
    name: "virtual_memory"
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Virtual Memory'
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
                    text: "Virtual Memory"             #TITLE NG NAV DOCK
                    halign: "center"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRaisedButton:
                    text: 'Demand Paging'                   #demand paging button
                    size_hint_x: 1
                    on_release:
                        root.demand_paging_pressed()

                MDRaisedButton:                    #Paged Segmentation button
                    text: 'Paged Segmentation'
                    size_hint_x: 1
                    on_release:
                        root.paged_segmentation_pressed()

                MDRaisedButton:
                    text: 'Demand Segmentation'             #Demand segmentation button
                    size_hint_x: 1
                    on_release:
                        root.demand_segmentation_pressed()
                
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


class Virtual_Memory_Screen(MDScreen):
    def demand_paging_pressed(self):
        print("Demand Paging Button Pressed")

    def paged_segmentation_pressed(self):
        print("Paged Segmentation Button Pressed")

    def demand_segmentation_pressed(self):
        print("Demand Segmentation Button Pressed")
