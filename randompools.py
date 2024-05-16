#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, simpledialog, filedialog
import random
import csv

class TeamPoolGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.dark_mode = True  # Set default mode to dark
        self.manual_entry = True  # Set default entry method to manual
        self.initialize_gui()

    def initialize_gui(self):
        self.title("Team Pool Generator")
        self.geometry("720x320")

        self.create_widgets()
        self.toggle_mode()  # Apply initial theme

    def create_widgets(self):
        self.team_canvas = tk.Canvas(self)
        self.team_canvas.grid(row=1, column=1)

        self.team_frame = ttk.Frame(self.team_canvas)
        self.team_canvas.create_window((0, 0), window=self.team_frame, anchor="nw")

        self.entry_choice_label = ttk.Label(self, text="Choose entry method:")
        self.entry_choice_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.manual_entry_radio = ttk.Radiobutton(self, text="Manual Entry", variable=self.manual_entry, value=True)
        self.manual_entry_radio.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.file_upload_radio = ttk.Radiobutton(self, text="File Upload", variable=self.manual_entry, value=False)
        self.file_upload_radio.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.team_name_entries = []
        for i in range(16):
            entry = ttk.Entry(self.team_frame, width=50)
            entry.grid(row=i, column=0, padx=5, pady=5)
            self.team_name_entries.append(entry)

        self.add_more_teams_button = ttk.Button(self, text="Add More Teams", command=self.add_more_teams)
        self.add_more_teams_button.grid(row=2, column=1, padx=5, pady=5)

        self.group_size_label = ttk.Label(self, text="Enter group size:")
        self.group_size_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.group_size_entry = ttk.Entry(self)
        self.group_size_entry.grid(row=3, column=1, padx=5, pady=5)

        self.num_groups_label = ttk.Label(self, text="Enter number of groups:")
        self.num_groups_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.num_groups_entry = ttk.Entry(self)
        self.num_groups_entry.grid(row=4, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(self, text="Generate Groups", command=self.generate_groups)
        self.submit_button.grid(row=5, column=1, padx=5, pady=5)

        self.mode_button = ttk.Button(self, text="Dark Mode", command=self.toggle_mode)
        self.mode_button.grid(row=0, column=3, padx=5, pady=5)

        # Add horizontal scrollbar
        self.horizontal_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.team_canvas.xview)
        self.horizontal_scrollbar.grid(row=6, column=1, sticky="ew")
        self.team_canvas.configure(xscrollcommand=self.horizontal_scrollbar.set)

        # Add vertical scrollbar
        self.vertical_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.team_canvas.yview)
        self.vertical_scrollbar.grid(row=1, column=2, sticky="ns")
        self.team_canvas.configure(yscrollcommand=self.vertical_scrollbar.set)

        # Add download button
        self.download_button = ttk.Button(self, text="Download Groups", command=self.download_groups)
        self.download_button.grid(row=5, column=0, padx=5, pady=5)

        # Add upload button
        self.upload_button = ttk.Button(self, text="Upload File", command=self.upload_file)
        self.upload_button.grid(row=6, column=0, padx=5, pady=5)

    def toggle_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.mode_button.configure(text="Light Mode")
        else:
            self.mode_button.configure(text="Dark Mode")

        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            self.configure(bg='black')
            self.team_frame.configure(style='Dark.TFrame')
            for entry in self.team_name_entries:
                entry.configure(style='Dark.TEntry')
            self.submit_button.configure(style='Dark.TButton')
            self.mode_button.configure(style='Dark.TButton')
            self.download_button.configure(style='Dark.TButton')
            self.upload_button.configure(style='Dark.TButton')
        else:
            self.configure(bg='white')
            self.team_frame.configure(style='Light.TFrame')
            for entry in self.team_name_entries:
                entry.configure(style='Light.TEntry')
            self.submit_button.configure(style='Light.TButton')
            self.mode_button.configure(style='Light.TButton')
            self.download_button.configure(style='Light.TButton')
            self.upload_button.configure(style='Light.TButton')

    def add_more_teams(self):
        add_window = tk.Toplevel(self)
        add_window.title("Add More Teams")
        add_window.geometry("400x400")

        add_team_name_entries = []
        for i in range(32):
            entry = ttk.Entry(add_window, width=50)
            entry.grid(row=i, column=0, padx=5, pady=5)
            add_team_name_entries.append(entry)

    def generate_groups(self):
        if self.manual_entry:
            team_names = [entry.get().strip() for entry in self.team_name_entries if entry.get().strip()]
        else:
            # Call a function to read data from the uploaded file
            team_names = self.read_uploaded_file()

        group_size = int(self.group_size_entry.get())
        num_groups = int(self.num_groups_entry.get())
        num_teams = len(team_names)

        # Shuffle the teams randomly
        random.shuffle(team_names)

        # Divide the teams into groups
        groups = [team_names[i:i+group_size] for i in range(0, num_teams, group_size)]

        # Add empty teams to the last group if necessary
        if len(groups[-1]) < group_size:
            groups[-1] += [''] * (group_size - len(groups[-1]))

        # Truncate extra groups if there are more than num_groups
        groups = groups[:num_groups]

        # Display the results in a new window
        result_window = tk.Toplevel(self)
        result_window.title("Team Pools")
        result_text = tk.Text(result_window, wrap="word", height=20, width=50)
        result_text.pack(padx=10, pady=10)

        result_text.insert(tk.END, "Team Pools\n\n")
        for i, group in enumerate(groups, 1):
            result_text.insert(tk.END, f"Group {i}:\n")
            for team in group:
                result_text.insert(tk.END, f"- {team}\n")
            result_text.insert(tk.END, "\n")

    def download_groups(self):
        pass

    def upload_file(self):
        pass

    def read_uploaded_file(self):
        pass

if __name__ == "__main__":
    app = TeamPoolGenerator()
    app.mainloop()