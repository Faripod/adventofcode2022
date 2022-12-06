value_dict = {
    "opponent": {
        "A": {"name":"rock", "value": 1},
        "B": {"name":"paper", "value": 2},
        "C": {"name":"scissor", "value": 3},
        },
    "you": {
        "X": {"name":"rock", "value": 1},
        "Y": {"name":"paper", "value": 2},
        "Z": {"name":"scissor", "value": 3},
        },
    "match": {
        "win": 6,
        "draw": 3,
        "lose": 0
        }
    }
# Read each line of txt file
file = open("input.txt", "r")

def match_result(opponent, you):
    if opponent == you:
        return "draw"
    if you == "rock":
        if opponent == "paper":
            return "lose"
        else:
            return "win"
    if you == "paper":
        if opponent == "scissor":
            return "lose"
        else:
            return "win"
    if you == "scissor":
        if opponent == "rock":
            return "lose"
        else:
            return "win"

def game(opponent, you):
    opponent_choose = value_dict['opponent'][opponent]["name"]
    you_choose = value_dict['you'][you]["name"]
    game_point = value_dict["you"][you]["value"]
    match_outcome = match_result(opponent_choose, you_choose)


    return game_point + value_dict["match"][match_outcome]

total_point = 0
for line in file:
    # clean txt
    line = line.replace("\n", "")
    list_of_plays = line.split(" ")
    total_point += game(list_of_plays[0], list_of_plays[1])

print(f'The total collected point are {total_point}')