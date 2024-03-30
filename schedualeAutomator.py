#!/usr/bin/env python3

import os
import random

# Define the file path to read team names from
file_path = "team_names.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Read team names from the text file
    with open(file_path, "r") as file:
        teams = [line.strip() for line in file.readlines()]

    # Shuffle the teams randomly
    random.shuffle(teams)

    # Divide teams into 4 groups
    num_groups = 4
    teams_per_group = len(teams) // num_groups
    groups = {"Pool A": [], "Pool B": [], "Pool C": [], "Pool D": []}

    for i in range(num_groups):
        group_name = f"Pool {chr(ord('A') + i)}"
        groups[group_name] = teams[i * teams_per_group:(i + 1) * teams_per_group]

    # Print groups
    print("Groups:")
    for group, teams_in_group in groups.items():
        print(f"{group}: {', '.join(teams_in_group)}")

    class PoolSchedule:
        def __init__(self, teams):
            self.teams = teams

        def generate_schedule(self, pool_name, start_time, num_games):
            print(f"{pool_name}:")
            current_time = start_time
            game_duration = 55  # Assuming each game lasts 55 minutes (45 minutes game time + 10 minutes break)
            for i in range(1, num_games + 1):
                team1 = self.teams[(i - 1) % len(self.teams)]
                team2 = self.teams[i % len(self.teams)]
                start_hour = current_time // 60
                start_minute = current_time % 60
                end_time = current_time + game_duration
                end_hour = end_time // 60
                end_minute = end_time % 60
                print(
                    f"{start_hour:02}:{start_minute:02} - {end_hour:02}:{end_minute:02} Uhr: Game {i} ({team1} vs. {team2})")
                current_time += game_duration
                if current_time >= 18 * 60 + 5:
                    break
                current_time += 45  # Add 45 minutes break after each game
            print()

    # Variables for the teams in each pool
    teams_pool_a = groups["Pool A"]
    teams_pool_b = groups["Pool B"]
    teams_pool_c = groups["Pool C"]
    teams_pool_d = groups["Pool D"]

    # Creating PoolSchedule instances for each pool
    pool_a_schedule = PoolSchedule(teams_pool_a)
    pool_b_schedule = PoolSchedule(teams_pool_b)
    pool_c_schedule = PoolSchedule(teams_pool_c)
    pool_d_schedule = PoolSchedule(teams_pool_d)

    # Generating schedule for each pool
    pool_a_schedule.generate_schedule("Pool A", 9 * 60, 5)
    pool_b_schedule.generate_schedule("Pool B", 9 * 60, 5)
    pool_c_schedule.generate_schedule("Pool C", 9 * 60, 5)
    pool_d_schedule.generate_schedule("Pool D", 9 * 60, 5)

    pool_a_schedule.generate_schedule("Pool A (Afternoon)", 14 * 60, 5)
    pool_b_schedule.generate_schedule("Pool B (Afternoon)", 14 * 60, 5)
    pool_c_schedule.generate_schedule("Pool C (Afternoon)", 14 * 60, 5)
    pool_d_schedule.generate_schedule("Pool D (Afternoon)", 14 * 60, 5)
else:
    print(f"Error: '{file_path}' file not found.")
