#! usr/env/bin/env python3

team_names = [
    "$1", "§2", "$3", "$4", "$5","$6", "$7", "$8", "$9", "$10","$11", "$12", "$13", "$14", "$15", "$16","$17", "$18", "$19", "$20"
]

# Define the file path
file_path = "team_names.txt"

# Write the team names to the file
with open(file_path, "w") as file:
    for team in team_names:
        file.write(team + "\n")

print("Team names have been written to", file_path)