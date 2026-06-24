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
                        text: "GANNT CHART"
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

        qt = self.ids.quantum_time.text.strip()

        process = {
            "pid": pid,
            "at": int(at),
            "bt": int(bt),
            "priority": int(priority) if priority else 0,
            "qt": int(qt) if qt else 0
        }

        self.processes.append(process)

        table = self.ids.table_layout

        table.add_widget(MDLabel(text=pid))
        table.add_widget(MDLabel(text=at))
        table.add_widget(MDLabel(text=bt))
        table.add_widget(MDLabel(text=priority if priority else "0"))
        table.add_widget(MDLabel(
        text=self.ids.quantum_time.text if self.ids.quantum_time.text else "-"
    ))

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

        # Initial time
        self.ids.gantt_times.add_widget(
            MDLabel(
                text=str(current_time),
                size_hint_x=None,
                width=40,
                halign="left"
            )
        )

        for p in processes:

            if current_time < p["at"]:
                current_time = p["at"]

            start_time = current_time
            end_time = p["at"] + p["bt"]

            box_width = max(80, p["bt"] * 40)

            # Create the Gantt box
            process_box = MDCard(
                size_hint=(None, None),
                width=box_width,
                height=60,
                radius=[0, 0, 0, 0],
                elevation=1,
            )

            process_box.add_widget(
                MDLabel(
                    text=p["pid"],
                    halign="center",
                    valign="middle",
                    text_size=(box_width, 60),
                )
            )

            self.ids.gantt_boxes.add_widget(process_box)

            # Add ending time under the box
            self.ids.gantt_times.add_widget(
                MDLabel(
                    text=str(end_time),
                    size_hint_x=None,
                    width=box_width,
                    halign="right",
                )
            )

            current_time = end_time


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

        if len(self.processes) == 0:
            return

        processes = []

        for p in self.processes:
            processes.append({
                "pid": p["pid"],
                "at": p["at"],
                "bt": p["bt"],
                "priority": p["priority"],
                "remaining": p["bt"]
            })

        current_time = 0
        completed = 0
        n = len(processes)

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
                key=lambda p: p["priority"]
            )

            current["remaining"] -= 1
            current_time += 1

            if current["remaining"] == 0:

                completed += 1

                finish = current_time

                tat = finish - current["at"]
                wt = tat - current["bt"]

                current["tat"] = tat
                current["wt"] = wt

        avg_waiting = sum(p["wt"] for p in processes) / n
        avg_turnaround = sum(p["tat"] for p in processes) / n

        self.ids.waiting_time.text = f"{avg_waiting:.2f} ms"
        self.ids.turnaround_time.text = f"{avg_turnaround:.2f} ms"

    def priority_nonpreemptive_pressed(self):

        if len(self.processes) == 0:
            return

        processes = [p.copy() for p in self.processes]

        completed = []
        current_time = 0

        total_waiting = 0
        total_turnaround = 0

        gantt = []

        while len(completed) < len(processes):

            available = [
                p for p in processes
                if p not in completed and p["at"] <= current_time
            ]

            if not available:
                current_time += 1
                continue

            highest = min(
                available,
                key=lambda p: p["priority"]
            )

            waiting = current_time - highest["at"]
            turnaround = waiting + highest["bt"]

            highest["wt"] = waiting
            highest["tat"] = turnaround

            total_waiting += waiting
            total_turnaround += turnaround

            gantt.append(highest)

            current_time += highest["bt"]

            completed.append(highest)

        avg_waiting = total_waiting / len(processes)
        avg_turnaround = total_turnaround / len(processes)

        self.ids.waiting_time.text = f"{avg_waiting:.2f} ms"
        self.ids.turnaround_time.text = f"{avg_turnaround:.2f} ms"

        self.draw_gantt_chart(gantt)

    def rr_pressed(self):

        if len(self.processes) == 0:
            return

        quantum_text = self.ids.quantum_time.text.strip()

        if quantum_text == "":
            print("Enter Quantum Time")
            return

        quantum = int(quantum_text)

        processes = []

        for p in self.processes:
            processes.append({
                "pid": p["pid"],
                "at": p["at"],
                "bt": p["bt"],
                "remaining": p["bt"]
            })

        processes.sort(key=lambda x: x["at"])

        current_time = 0
        completed = 0
        n = len(processes)

        queue = []
        gantt = []

        i = 0

        while completed < n:

            while i < n and processes[i]["at"] <= current_time:
                queue.append(processes[i])
                i += 1

            if not queue:
                current_time += 1
                continue

            current = queue.pop(0)

            start = current_time

            execution = min(
                quantum,
                current["remaining"]
            )

            current_time += execution

            current["remaining"] -= execution

            gantt.append({
                "pid": current["pid"],
                "bt": execution,
                "at": start
            })

            while i < n and processes[i]["at"] <= current_time:
                queue.append(processes[i])
                i += 1

            if current["remaining"] > 0:

                queue.append(current)

            else:

                completed += 1

                finish = current_time

                tat = finish - current["at"]
                wt = tat - current["bt"]

                current["tat"] = tat
                current["wt"] = wt

        avg_wt = sum(p["wt"] for p in processes) / n
        avg_tat = sum(p["tat"] for p in processes) / n

        self.ids.waiting_time.text = f"{avg_wt:.2f} ms"
        self.ids.turnaround_time.text = f"{avg_tat:.2f} ms"

        self.draw_gantt_chart(gantt)
