from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivymd.uix.card import MDCard



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
                    text: 'FIFO'                   #FIFO page replacement button
                    size_hint_x: 1
                    on_release:
                        root.fifo_page_replacement_pressed()

                MDRaisedButton:                    #Optimal page replacement button
                    text: 'Optimal'
                    size_hint_x: 1
                    on_release:
                        root.optimal_page_replacement_pressed()

                MDRaisedButton:
                    text: 'LRU'             #LRU segmentation button
                    size_hint_x: 1
                    on_release:
                        root.lru_page_replacement_pressed()

                MDRaisedButton:
                    text: 'LRU Approximation'             #LRU Approximation button
                    size_hint_x: 1
                    on_release:
                        root.lru_approximation_page_replacement_pressed()

                MDRaisedButton:
                    text: 'Counting Based'             #Counting Based button
                    size_hint_x: 1
                    on_release:
                        root.counting_based_page_replacement_pressed()
                
                MDRaisedButton:
                    text: 'CLEAR'     # CLEAR BUTTON
                    size_hint_x: 1
                    on_release:
                        root.clear_pressed()

                Widget:

            # --------------------------
            # MAIN CONTENT (80%)
            # --------------------------

            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: 0.8
                padding: dp(20)
                spacing: dp(10)

                # --------------------------
                # INPUT AREA (15%)
                # --------------------------
                MDCard:
                    size_hint_y: 0.15
                    radius: [15]
                    elevation: 3
                    padding: dp(10)

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)

                        # Input Box
                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: dp(10)

                            MDTextField:
                                id: disk_queue_input
                                hint_text: "Enter page reference string"
                                mode: "rectangle"

                        # Result Box
                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: dp(10)

                            MDTextField:
                                id: num_frames_input
                                hint_text: "Enter number of frames"
                                mode: "rectangle"



                # --------------------------
                # OUTPUT AREA (85%)
                # --------------------------
                MDCard:
                    size_hint_y: 0.85
                    radius: [15]
                    elevation: 3
                    padding: dp(10)

                    ScrollView:

                        MDBoxLayout:
                            id: output_box
                            orientation: "vertical"
                            size_hint_y: None
                            height: self.minimum_height
                            spacing: dp(20)
                            padding: dp(10)
                            
'''

Builder.load_string(KV)


class Virtual_Memory_Screen(MDScreen):

    def fifo_page_replacement_pressed(self):
        self.ids.output_box.clear_widgets()

        try:
            pages = self.ids.disk_queue_input.text.replace(",", " ").split()
            frames_count = int(self.ids.num_frames_input.text)
        except ValueError:
            return

        # Show reference string
        self.show_reference_string()

        # Create boxes
        self.box_maker()

        # FIFO Simulation
        frames = [""] * frames_count
        fifo_index = 0
        history = []

        for page in pages:

            if page not in frames:
                frames[fifo_index] = page
                fifo_index = (fifo_index + 1) % frames_count

            history.append(frames.copy())

        # Put values into boxes
        for col in range(len(history)):
            for row in range(frames_count):
                self.cells[row][col].text = str(history[col][row])

        
    def optimal_page_replacement_pressed(self):
        self.ids.output_box.clear_widgets()

        try:
            pages = self.ids.disk_queue_input.text.replace(",", " ").split()
            frames_count = int(self.ids.num_frames_input.text)
        except ValueError:
            return

        self.show_reference_string()
        self.box_maker()

        frames = [""] * frames_count
        history = []

        for i, page in enumerate(pages):

            # HIT
            if page in frames:
                history.append(frames.copy())
                continue

            # Empty frame available
            if "" in frames:
                empty_index = frames.index("")
                frames[empty_index] = page

            else:
                # OPTIMAL replacement
                future_use = []

                for frame_page in frames:

                    if frame_page in pages[i + 1:]:
                        next_use = pages[i + 1:].index(frame_page)
                    else:
                        next_use = float('inf')

                    future_use.append(next_use)

                replace_index = future_use.index(max(future_use))
                frames[replace_index] = page

            history.append(frames.copy())

        # Fill boxes
        for col in range(len(history)):
            for row in range(frames_count):
                self.cells[row][col].text = str(history[col][row])

 
    def lru_page_replacement_pressed(self):
        self.ids.output_box.clear_widgets()

        try:
            pages = self.ids.disk_queue_input.text.replace(",", " ").split()
            frames_count = int(self.ids.num_frames_input.text)
        except ValueError:
            return

        self.show_reference_string()
        self.box_maker()

        frames = [""] * frames_count
        history = []
        faults = 0

        for i, page in enumerate(pages):

            # HIT
            if page in frames:
                history.append(frames.copy())
                continue

            faults += 1

            # Empty frame available
            if "" in frames:
                empty_index = frames.index("")
                frames[empty_index] = page

            else:
                # Find Least Recently Used page
                last_used = []

                for frame_page in frames:
                    last_index = -1

                    for j in range(i - 1, -1, -1):
                        if pages[j] == frame_page:
                            last_index = j
                            break

                    last_used.append(last_index)

                replace_index = last_used.index(min(last_used))
                frames[replace_index] = page

            history.append(frames.copy())

        # Fill boxes
        for col in range(len(history)):
            for row in range(frames_count):
                self.cells[row][col].text = str(history[col][row])

        # Show page faults
        self.ids.output_box.add_widget(
            MDLabel(
                text=f"Page Faults: {faults}",
                halign="center",
                size_hint_y=None,
                height=dp(40),
                bold=True
            )
        )

    def lru_approximation_page_replacement_pressed(self):
        self.ids.output_box.clear_widgets()

        try:
            pages = self.ids.disk_queue_input.text.replace(",", " ").split()
            frames_count = int(self.ids.num_frames_input.text)
        except ValueError:
            return

        self.show_reference_string()
        self.box_maker()

        frames = [""] * frames_count
        reference_bits = [0] * frames_count
        pointer = 0

        history = []
        faults = 0

        for page in pages:

            # HIT
            if page in frames:
                index = frames.index(page)
                reference_bits[index] = 1
                history.append(frames.copy())
                continue

            faults += 1

            # Empty frame available
            if "" in frames:
                empty_index = frames.index("")
                frames[empty_index] = page
                reference_bits[empty_index] = 1

            else:
                # Second Chance replacement
                while True:

                    if reference_bits[pointer] == 0:
                        frames[pointer] = page
                        reference_bits[pointer] = 1
                        pointer = (pointer + 1) % frames_count
                        break

                    reference_bits[pointer] = 0
                    pointer = (pointer + 1) % frames_count

            history.append(frames.copy())

        # Fill boxes
        for col in range(len(history)):
            for row in range(frames_count):
                self.cells[row][col].text = str(history[col][row])

        # Page fault count
        self.ids.output_box.add_widget(
            MDLabel(
                text=f"Page Faults: {faults}",
                halign="center",
                size_hint_y=None,
                height=dp(40),
                bold=True
            )
        )
        
    def counting_based_page_replacement_pressed(self):
        self.ids.output_box.clear_widgets()

        try:
            pages = self.ids.disk_queue_input.text.replace(",", " ").split()
            frames_count = int(self.ids.num_frames_input.text)
        except ValueError:
            return

        self.show_reference_string()
        self.box_maker()

        frames = [""] * frames_count
        frequency = {}
        history = []
        faults = 0

        for page in pages:

            frequency[page] = frequency.get(page, 0) + 1

            # HIT
            if page in frames:
                history.append(frames.copy())
                continue

            faults += 1

            # Empty frame
            if "" in frames:
                empty_index = frames.index("")
                frames[empty_index] = page

            else:
                # LFU replacement
                min_freq = float('inf')
                replace_index = 0

                for i, frame_page in enumerate(frames):
                    if frequency[frame_page] < min_freq:
                        min_freq = frequency[frame_page]
                        replace_index = i

                frames[replace_index] = page

            history.append(frames.copy())

        # Fill boxes
        for col in range(len(history)):
            for row in range(frames_count):
                self.cells[row][col].text = str(history[col][row])

        # Page fault count
        self.ids.output_box.add_widget(
            MDLabel(
                text=f"Page Faults: {faults}",
                halign="center",
                size_hint_y=None,
                height=dp(40),
                bold=True
            )
        )


    def show_reference_string(self):
        output_box = self.ids.output_box

        pages = self.ids.disk_queue_input.text.replace(",", " ").split()

        row = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(40),
            spacing=dp(2)
        )

        for page in pages:
            row.add_widget(
                MDLabel(
                    text=page,
                    halign="center",
                    size_hint_x=1,
                    bold=True
                )
            )

        output_box.add_widget(row)

    def clear_pressed(self):
        self.ids.disk_queue_input.text = ""
        self.ids.num_frames_input.text = ""
        self.ids.output_box.clear_widgets()


    def box_maker(self):
        output_box = self.ids.output_box

        pages = self.ids.disk_queue_input.text.replace(",", " ").split()

        try:
            frames = int(self.ids.num_frames_input.text)
        except ValueError:
            return

        self.cells = []

        grid = GridLayout(
            cols=len(pages),
            rows=frames,
            size_hint_y=None,
            spacing=dp(2),
            row_default_height=dp(40),
            row_force_default=True
        )

        grid.height = frames * dp(42)

        for row in range(frames):

            row_cells = []

            for col in range(len(pages)):

                label = MDLabel(
                    text="",
                    halign="center"
                )

                cell = MDCard(
                    style="outlined",
                    size_hint_y=None,
                    height=dp(40),
                    radius=[0],
                    elevation=0
                )

                cell.add_widget(label)

                grid.add_widget(cell)

                row_cells.append(label)

            self.cells.append(row_cells)

        output_box.add_widget(grid)
