#!/usr/bin/env python3


import random
import os

# List of team names
team_names = [
    "Heidees", "Bad Raps", "Prinz Hessinen", "Pizza Volante", "FT Würzburg",
    "1. FC Frisbeelarrys", "Mainz Ultimate", "Square Force", "Maultaschen", "gOLDbären",
    "Bonnsai", "Colorado", "MINT", "Air Support", "Big Fans & Friends", "Lobstars",
    "Wurfkultur", "Nullacht Ultimate", "Skid Ultimate", "Disconnction"
]

# Shuffle the teams
random.shuffle(team_names)

# Grouping
num_groups = 4
group_size = len(team_names) // num_groups
groups = [team_names[i * group_size:(i + 1) * group_size] for i in range(num_groups)]

# Distribute remaining teams
remaining_teams = team_names[num_groups * group_size:]
for i, team in enumerate(remaining_teams):
    groups[i % num_groups].append(team)

# Output the teams in groups with numbering
group_names = ['A', 'B', 'C', 'D']
for i, (group, group_name) in enumerate(zip(groups, group_names), start=0):
    print(f"Group {group_name}:")
    for j, team in enumerate(group, start=1):
        print(f"{group_name}{j}. {team}")