# Read each line of txt file
file = open("input.txt", "r")
most_calories = 0
tmp_calories = 0

for line in file:
    if line != "\n":
        tmp_calories += int(line)
    else:
        most_calories = max(most_calories, tmp_calories)
        tmp_calories = 0
# handle last line

print(f'The elf with most calories have => {most_calories}')