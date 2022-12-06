#  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
value_dict = {
        "A": {"X": 3 + 0, "Y": 1 + 3, "Z": 2 + 6},
        "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
        "C": {"X": 2 + 0, "Y": 3 + 3, "Z": 1 + 6}
        }
# Read each line of txt file
file = open("input.txt", "r")

total_point = 0
for line in file:
    # clean txt
    line = line.replace("\n", "")
    list_of_plays = line.split(" ")
    total_point += value_dict[list_of_plays[0]][list_of_plays[1]]

print(f'The total collected point are {total_point}')