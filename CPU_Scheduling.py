from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<CPU_Scheduling_Screen>:
    name: "cpu_scheduling"

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'CPU Scheduling'
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

                MDRaisedButton:                    #SJF button
                    text: 'SJF (Pre-Emptive)'
                    size_hint_x: 1
                    on_release:
                        root.sjf_preemptive_pressed()

                MDRaisedButton:                    #SJF button
                    text: 'SJF (non-Pre-Emptive)'
                    size_hint_x: 1
                    on_release:
                        root.sjf_nonpreemptive_pressed()

                MDRaisedButton:                     #PRIORITY button
                    text: 'Priority(Pre-Emptive)'
                    size_hint_x: 1
                    on_release:
                        root.priority_preemptive_pressed()

                MDRaisedButton:                     #PRIORITY button
                    text: 'Priority(Non-Pre-Emptive)'
                    size_hint_x: 1
                    on_release:
                        root.priority_nonpreemptive_pressed()

                MDRaisedButton:
                    text: 'Round Robin'             #ROUND ROBIN button
                    size_hint_x: 1
                    on_release:
                        root.rr_pressed()

                MDRaisedButton:                     #CLEAR button
                    text: "Clear Table"
                    size_hint_x: 1
                    md_bg_color: 1, 0.2, 0.2, 1
                    on_release:
                        root.clear_table()
                                
                Widget:

            # --------------------------
            # MAIN CONTENT (80%)
            # --------------------------

            MDBoxLayout:
                orientation: "vertical"
                size_hint_x: 0.8
                padding: dp(20)
                spacing: dp(20)


                # TABLE NG PROCESS
                MDCard:
                    orientation: "vertical"

                    ScrollView:
                        GridLayout:
                            id: table_layout
                            cols: 5
                            size_hint_y: None
                            height: self.minimum_height

                            # IMPORTANT FIXES ↓↓↓
                            row_default_height: dp(45)
                            row_force_default: True


                            spacing: dp(12)

                            # HEADER ROW
                            MDLabel:
                                text: "Process"
                                halign: "center"
                                valign: "middle"
                                text_size: self.size

                            MDLabel:
                                text: "Arrival Time"
                                halign: "center"
                                valign: "middle"
                                text_size: self.size

                            MDLabel:
                                text: "Burst Time"
                                halign: "center"
                                valign: "middle"
                                text_size: self.size

                            MDLabel:
                                text: "Priority"
                                halign: "center"
                                valign: "middle"
                                text_size: self.size

                            MDLabel:
                                text: "Quantum Time"
                                halign: "center"
                                valign: "middle"
                                text_size: self.size

                            # INPUT ROW (ALIGNED UNDER HEADER)
                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(4)

                                MDRaisedButton:
                                    text: "Add Process"
                                    pos_hint: {"center_y": .5}
                                    on_release: root.add_process()

                            MDTextField:
                                id: at_input
                                hint_text: "AT"
                                input_filter: "int"

                            MDTextField:
                                id: bt_input
                                hint_text: "BT"
                                input_filter: "int"

                            MDTextField:
                                id: priority_input
                                hint_text: "Priority"
                                input_filter: "int"

                            MDTextField:
                                id: quantum_time
                                hint_text: "QT"
                                input_filter: "int"
                                        
                # GANNT CHART
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)

                    MDLabel:
                        text: "Gantt Chart"
                        halign: "center"

                    MDBoxLayout:
                        id: gantt_container
                        orientation: "vertical"
                        spacing: dp(2)

                        MDBoxLayout:
                            id: gantt_boxes
                            orientation: "horizontal"
                            size_hint_y: None
                            height: dp(60)
                            spacing: 0

                        MDBoxLayout:
                            id: gantt_times
                            orientation: "horizontal"
                            size_hint_y: None
                            height: dp(25)
                            spacing: 0
                                    
                # TURNAROUND TIME & WAITING TIME
                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: dp(15)
                    size_hint_y: 0.3

                    # TURNAROUND TIME
                    MDCard:
                        orientation: "vertical"
                        radius: [10,10,10,10]
                        elevation: 1
                        padding: dp(10)
                        md_bg_color: 0.95, 0.95, 0.95, 1

                        MDLabel:
                            text: "Turnaround Time"
                            halign: "center"
                            bold: True

                        MDLabel:
                            id: turnaround_time
                            text: "0 ms"
                            halign: "center"
                            font_style: "H5"

                    # WAITING TIME
                    MDCard:
                        orientation: "vertical"
                        radius: [10,10,10,10]
                        elevation: 1
                        padding: dp(10)
                        md_bg_color: 0.95, 0.95, 0.95, 1

                        MDLabel:
                            text: "Waiting Time"
                            halign: "center"
                            bold: True

                        MDLabel:
                            id: waiting_time
                            text: "0 ms"
                            halign: "center"
                            font_style: "H5"
                            
                            Widget:
'''

Builder.load_string(KV)



class CPU_Scheduling_Screen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.processes = []
        self.process_counter = 1

    def add_process(self):

        at = self.ids.at_input.text.strip()
        bt = self.ids.bt_input.text.strip()
        priority = self.ids.priority_input.text.strip()

        if at == "" or bt == "":
            return

        pid = f"P{self.process_counter}"

        process = {
            "pid": pid,
            "at": int(at),
            "bt": int(bt),
            "priority": int(priority) if priority else 0
        }

        self.processes.append(process)

        table = self.ids.table_layout

        table.add_widget(MDLabel(text=pid))
        table.add_widget(MDLabel(text=at))
        table.add_widget(MDLabel(text=bt))
        table.add_widget(MDLabel(text=priority if priority else "0"))
        table.add_widget(MDLabel(text="-"))

        self.process_counter += 1

        self.ids.at_input.text = ""
        self.ids.bt_input.text = ""
        self.ids.priority_input.text = ""

        print("Added:", process)

    def clear_table(self):

        self.processes.clear()
        self.process_counter = 1

        table = self.ids.table_layout

        # Remove added process rows
        while len(table.children) > 10:
            table.remove_widget(table.children[0])

        # Clear inputs
        self.ids.at_input.text = ""
        self.ids.bt_input.text = ""
        self.ids.priority_input.text = ""
        self.ids.quantum_time.text = ""

        # Reset results
        self.ids.waiting_time.text = "0 ms"
        self.ids.turnaround_time.text = "0 ms"

        # Clear Gantt Chart
        self.ids.gantt_boxes.clear_widgets()
        self.ids.gantt_times.clear_widgets()

        print("Table Cleared")


    def draw_gantt_chart(self, processes):

        self.ids.gantt_boxes.clear_widgets()
        self.ids.gantt_times.clear_widgets()

        current_time = 0

        for index, p in enumerate(processes):

            if current_time < p["at"]:
                current_time = p["at"]

            start_time = current_time
            end_time = current_time + p["bt"]

            box_width = max(80, p["bt"] * 40)

            # PROCESS BOX
            box = MDCard(
                size_hint=(None, None),
                width=box_width,
                height=50,
                radius=[0, 0, 0, 0],
                style="outlined"
            )

            box.add_widget(
                MDLabel(
                    text=p["pid"],
                    halign="center",
                    valign="middle",
                    text_size=(box_width, 50)
                )
            )

            self.ids.gantt_boxes.add_widget(box)

            # START TIME
            time_label = MDLabel(
                text=str(start_time),
                size_hint=(None, 1),
                width=box_width,
                halign="left"
            )

            self.ids.gantt_times.add_widget(time_label)

            current_time = end_time

        # FINAL TIME
        self.ids.gantt_times.add_widget(
            MDLabel(
                text=str(current_time),
                size_hint=(None, 1),
                width=40,
                halign="left"
            )
        )

    def fcfs_pressed(self):

        if len(self.processes) == 0:
            self.ids.waiting_time.text = "0 ms"
            self.ids.turnaround_time.text = "0 ms"
            return

        processes = sorted(
            self.processes,
            key=lambda p: p["at"]
        )

        current_time = 0
        total_waiting = 0
        total_turnaround = 0

        for p in processes:

            arrival = p["at"]
            burst = p["bt"]

            if current_time < arrival:
                current_time = arrival

            waiting = current_time - arrival
            turnaround = waiting + burst

            current_time += burst

            total_waiting += waiting
            total_turnaround += turnaround

            print(
                p["pid"],
                "WT =", waiting,
                "TAT =", turnaround
            )

        avg_waiting = total_waiting / len(processes)
        avg_turnaround = total_turnaround / len(processes)

        self.ids.waiting_time.text = f"{avg_waiting:.2f} ms"
        self.ids.turnaround_time.text = f"{avg_turnaround:.2f} ms"
        self.draw_gantt_chart(processes)


    def sjf_preemptive_pressed(self):

        if len(self.processes) == 0:
            self.ids.waiting_time.text = "0 ms"
            self.ids.turnaround_time.text = "0 ms"
            return

        processes = []

        for p in self.processes:
            processes.append({
                "pid": p["pid"],
                "at": p["at"],
                "bt": p["bt"],
                "remaining": p["bt"]
            })

        current_time = 0
        completed = 0
        n = len(processes)

        gantt = []

        while completed < n:

            available = [
                p for p in processes
                if p["at"] <= current_time and p["remaining"] > 0
            ]

            if not available:
                current_time += 1
                continue

            current = min(
                available,
                key=lambda p: p["remaining"]
            )

            gantt.append(current["pid"])

            current["remaining"] -= 1
            current_time += 1

            if current["remaining"] == 0:

                completed += 1

                finish_time = current_time

                tat = finish_time - current["at"]
                wt = tat - current["bt"]

                current["tat"] = tat
                current["wt"] = wt

        avg_waiting = sum(
            p["wt"] for p in processes
        ) / n

        avg_turnaround = sum(
            p["tat"] for p in processes
        ) / n

        self.ids.waiting_time.text = f"{avg_waiting:.2f} ms"
        self.ids.turnaround_time.text = f"{avg_turnaround:.2f} ms"

        print("Gantt:", gantt)

    def sjf_nonpreemptive_pressed(self):

        if len(self.processes) == 0:
            self.ids.waiting_time.text = "0 ms"
            self.ids.turnaround_time.text = "0 ms"
            return

        processes = [p.copy() for p in self.processes]

        completed = []
        current_time = 0

        total_waiting = 0
        total_turnaround = 0

        while len(completed) < len(processes):

            available = [
                p for p in processes
                if p not in completed and p["at"] <= current_time
            ]

            if not available:
                current_time += 1
                continue

            shortest = min(
                available,
                key=lambda p: p["bt"]
            )

            waiting = current_time - shortest["at"]
            turnaround = waiting + shortest["bt"]

            shortest["wt"] = waiting
            shortest["tat"] = turnaround

            total_waiting += waiting
            total_turnaround += turnaround

            current_time += shortest["bt"]

            completed.append(shortest)

        avg_waiting = total_waiting / len(processes)
        avg_turnaround = total_turnaround / len(processes)

        self.ids.waiting_time.text = f"{avg_waiting:.2f} ms"
        self.ids.turnaround_time.text = f"{avg_turnaround:.2f} ms"

        self.draw_gantt_chart(completed)

    def priority_preemptive_pressed(self):
        print("Priority (Pre-Emptive) Button Pressed")

    def priority_nonpreemptive_pressed(self):
        print("Priority (Non-Pre-Emptive) Button Pressed")

    def rr_pressed(self):
        print("Round Robin Button Pressed")

