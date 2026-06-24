from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.graphics import Color, Line, Ellipse, Rectangle
from kivy.core.text import Label as CoreLabel

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
                    text: "Algorithms"
                    halign: "center"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1

                MDRaisedButton:
                    text: 'FCFS'
                    size_hint_x: 1
                    on_release: root.fcfs_pressed()

                MDRaisedButton:
                    text: 'SSTF'
                    size_hint_x: 1
                    on_release: root.sstf_pressed()

                MDRaisedButton:
                    text: 'SCAN'
                    size_hint_x: 1
                    on_release: root.scan_pressed()

                MDRaisedButton:
                    text: 'C-SCAN'
                    size_hint_x: 1
                    on_release: root.cscan_pressed()

                MDRaisedButton:
                    text: 'LOOK'
                    size_hint_x: 1
                    on_release: root.look_pressed()

                MDRaisedButton:
                    text: 'CLEAR'
                    size_hint_x: 1
                    on_release: root.clear_pressed()

                Widget:

            # --------------------------
            # MAIN CONTENT (80%)
            # --------------------------
            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: 0.8
                padding: dp(20)
                spacing: dp(20)

                # INPUT SECTION
                MDCard:
                    orientation: "vertical"
                    size_hint_y: 0.15
                    padding: dp(10)
                    spacing: dp(10)
                    radius: [15,15,15,15]
                    elevation: 3

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)

                        MDTextField:
                            id: disk_queue_input
                            hint_text: "Disk Queue"
                            mode: "rectangle"

                        MDTextField:
                            id: header_input
                            hint_text: "Head Track:"
                            mode: "rectangle"

                # VISUALIZATION
                MDCard:
                    orientation: "vertical"
                    size_hint_y: 0.70
                    padding: dp(20)
                    spacing: dp(15)
                    radius: [15,15,15,15]
                    elevation: 3

                    Widget:
                        id: graph_widget

                # RESULT SECTION
                MDCard:
                    orientation: "vertical"
                    size_hint_y: 0.15
                    padding: dp(15)
                    spacing: dp(10)
                    radius: [15,15,15,15]
                    elevation: 3

                    MDLabel:
                        id: sequence_label
                        text: "Seek Sequence:"
                        halign: "left"
                
                    Widget:
'''

Builder.load_string(KV)


class Mass_Storage_Screen(MDScreen):
    DISK_MAX = 199  # Global standard upper boundary for track simulation

    def _get_inputs(self):
        """Helper to cleanly parse inputs dynamically."""
        requests = [
            int(x.strip())
            for x in self.ids.disk_queue_input.text.split(",")
            if x.strip().isdigit()
        ]
        head = int(self.ids.header_input.text or 0)
        return requests, head

    def fcfs_pressed(self):
        requests, head = self._get_inputs()
        sequence = [head] + requests
        self.update_graph(sequence)

    def sstf_pressed(self):
        requests, head = self._get_inputs()
        remaining = requests[:]
        sequence = [head]
        current = head

        while remaining:
            closest = min(remaining, key=lambda x: abs(x - current))
            sequence.append(closest)
            remaining.remove(closest)
            current = closest

        self.update_graph(sequence)

    def scan_pressed(self):
        requests = [
            int(x.strip())
            for x in self.ids.disk_queue_input.text.split(",")
            if x.strip()
        ]

        head = int(self.ids.header_input.text or 0)

        if not requests:
            return

        left = sorted([x for x in requests if x < head], reverse=True)
        right = sorted([x for x in requests if x >= head])

        sequence = [head]

        # STEP 1: go down to 0 through all left side
        sequence.extend(left)

        # force reach 0 (center boundary behavior you want)
        sequence.append(0)

        # STEP 2: from 0 go to highest right side
        sequence.extend(right)

        self.update_graph(sequence)

    def cscan_pressed(self):
        requests, head = self._get_inputs()
        if not requests:
            return

        left = sorted([x for x in requests if x < head])
        right = sorted([x for x in requests if x >= head])

        sequence = [head]

        # STEP 1: move upward first
        sequence.extend(right)

        # STEP 2: wrap directly to 0 (NO 199)
        if left:
            sequence.append(0)

        # STEP 3: continue upward from lowest side
        sequence.extend(left)

        self.update_graph(sequence)

    def look_pressed(self):
        requests, head = self._get_inputs()

        if not requests:
            return

        # Values >= head
        right = sorted([x for x in requests if x >= head])

        # Values < head
        left = sorted([x for x in requests if x < head])

        sequence = [head]

        # Head -> highest side
        sequence.extend(right)

        # Highest -> lowest -> continue upward
        sequence.extend(left)

        self.update_graph(sequence)


    def on_kv_post(self, *args):
        self.ids.graph_widget.bind(
            size=lambda *x: self.redraw_graph(),
            pos=lambda *x: self.redraw_graph()
        )

    def redraw_graph(self):
        if hasattr(self, "sequence"):
            self.draw_graph()

    def draw_graph(self, *args):
        if not hasattr(self, "sequence") or not self.sequence:
            return

        widget = self.ids.graph_widget
        widget.canvas.clear()

        if widget.width < 10 or widget.height < 10:
            return

        sequence = self.sequence

        with widget.canvas:
            Color(0.95, 0.95, 0.95, 1)
            Rectangle(pos=widget.pos, size=widget.size)

        left_margin = 60
        right_margin = 60
        top_margin = 50
        bottom_margin = 50

        usable_width = widget.width - left_margin - right_margin
        usable_height = widget.height - top_margin - bottom_margin

        step_y = usable_height / max(len(sequence) - 1, 1)

        # Base track bounds on standard system architecture rules (0 to 199)
        min_val = 0
        max_val = max(self.DISK_MAX, max(sequence))
        value_range = max(max_val - min_val, 1)

        points = []

        for i, value in enumerate(sequence):
            x = (
                widget.x
                + left_margin
                + ((value - min_val) / value_range) * usable_width
            )
            y = widget.y + top_margin + (len(sequence) - 1 - i) * step_y

            points.extend([x, y])

            with widget.canvas:
                Color(0, 0, 1, 1)
                Ellipse(pos=(x - 6, y - 6), size=(12, 12))

                Color(0, 0, 0, 1)
                label = CoreLabel(text=str(value), font_size=16)
                label.refresh()
                Rectangle(
                    texture=label.texture,
                    pos=(x + 10, y - 10),
                    size=label.texture.size
                )

        with widget.canvas:
            Color(0, 0, 0, 1)
            Line(points=points, width=1)

    def update_graph(self, sequence):
        self.sequence = sequence
        total_seek = sum(
            abs(sequence[i + 1] - sequence[i])
            for i in range(len(sequence) - 1)
        )

        self.ids.sequence_label.text = (
            f"Total Tracks: {total_seek}\n"
            f"{' -> '.join(map(str, sequence))}"
        )
        self.draw_graph()

    def clear_pressed(self):
        self.ids.disk_queue_input.text = ""
        self.ids.header_input.text = ""

        self.ids.sequence_label.text = "Seek Sequence:"

        self.ids.graph_widget.canvas.clear()

        if hasattr(self, "sequence"):
            del self.sequence

