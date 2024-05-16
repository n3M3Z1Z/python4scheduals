#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, simpledialog
import random

def generate_groups():
    team_names = [entry.get().strip() for entry in team_name_entries if entry.get().strip()]  # Remove empty lines
    group_size = int(group_size_entry.get())
    num_groups = int(num_groups_entry.get())
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
    result_window = tk.Toplevel(root)
    result_window.title("Team Pools")
    result_text = tk.Text(result_window, wrap="word", height=20, width=50, bg='#2E2E2E', fg='white')
    result_text.pack(padx=10, pady=10)
    
    result_text.insert(tk.END, "Team Pools\n\n")
    for i, group in enumerate(groups, 1):
        result_text.insert(tk.END, f"Group {i}:\n")
        for team in group:
            result_text.insert(tk.END, f"- {team}\n")
        result_text.insert(tk.END, "\n")

def add_more_rows():
    num_rows_to_add = int(simpledialog.askstring("Add Rows", "Enter the number of rows to add:"))
    if num_rows_to_add > 0:
        for _ in range(num_rows_to_add):
            entry = ttk.Entry(team_frame, width=50, style='Dark.TEntry')
            entry.grid(row=len(team_name_entries) + 1, column=1, padx=5, pady=5)
            team_name_entries.append(entry)

def add_more_teams():
    add_window = tk.Toplevel(root)
    add_window.title("Add More Teams")
    add_window.geometry("400x400")
    add_window.tk_setPalette(background='#2E2E2E', foreground='white', activeBackground='#4C4C4C', activeForeground='white')

    add_team_name_entries = []
    for i in range(32):
        entry = ttk.Entry(add_window, width=50, style='Dark.TEntry')
        entry.grid(row=i, column=0, padx=5, pady=5)
        add_team_name_entries.append(entry)

    add_more_rows_button = ttk.Button(add_window, text="Add More Rows", command=lambda: add_more_rows(), style='Dark.TButton')
    add_more_rows_button.grid(row=16, column=0, padx=5, pady=5)

# Create the main window
root = tk.Tk()
root.title("Team Pool Generator")

# Set the size of the GUI window to a 9:4 aspect ratio
root.geometry("720x320")

# Set dark mode theme
root.tk_setPalette(background='#2E2E2E', foreground='white', activeBackground='#4C4C4C', activeForeground='white')

# Create a canvas for the team name entries
team_canvas = tk.Canvas(root)
team_canvas.grid(row=1, column=1)

# Add a frame to the canvas to contain the team name entries
team_frame = ttk.Frame(team_canvas)
team_canvas.create_window((0, 0), window=team_frame, anchor="nw")

# Create and place labels and entry widgets for user input
teams_label = ttk.Label(root, text="Enter team names (one per line):", style='Dark.TLabel')
teams_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

team_name_entries = []
for i in range(16):
    entry = ttk.Entry(team_frame, width=50, style='Dark.TEntry')
    entry.grid(row=i, column=0, padx=5, pady=5)
    team_name_entries.append(entry)

add_more_teams_button = ttk.Button(root, text="Add More Teams", command=add_more_teams, style='Dark.TButton')
add_more_teams_button.grid(row=2, column=1, padx=5, pady=5)

group_size_label = ttk.Label(root, text="Enter group size:", style='Dark.TLabel')
group_size_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

group_size_entry = ttk.Entry(root, style='Dark.TEntry')
group_size_entry.grid(row=3, column=1, padx=5, pady=5)

num_groups_label = ttk.Label(root, text="Enter number of groups:", style='Dark.TLabel')
num_groups_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

num_groups_entry = ttk.Entry(root, style='Dark.TEntry')
num_groups_entry.grid(row=4, column=1, padx=5, pady=5)

submit_button = ttk.Button(root, text="Generate Groups", command=generate_groups, style='Dark.TButton')
submit_button.grid(row=5, column=1, padx=5, pady=5)

# Add horizontal scrollbar
horizontal_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=team_canvas.xview)
horizontal_scrollbar.grid(row=6, column=1, sticky="ew")
team_canvas.configure(xscrollcommand=horizontal_scrollbar.set)

# Add vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(root, orient="vertical", command=team_canvas.yview)
vertical_scrollbar.grid(row=1, column=2, sticky="ns")
team_canvas.configure(yscrollcommand=vertical_scrollbar.set)

# Start the Tkinter event loop
root.mainloop()