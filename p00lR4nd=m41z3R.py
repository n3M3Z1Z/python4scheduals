#!/usr/bin/env python3

# How to use this script

# Requirements: Python Tnerpreter 

# Replace $x in 'List of team names with the team names you need.
# Replace num_groups = x in ' Grouping with the number of pools you need.
# edit group_names = ['A', 'B', 'C', 'D'] in # Output the teams in groups with numbering so it fits for your specific needs

import random
import os

# List of team names
team_names = [
    "$1", "$2", "$3", "$4", "$5","$6", "$7", "$8", "$9", "$10","$11", "$12", "$13", "$14", "$15", "$16", "$17", "$18", "$19", "$20"
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