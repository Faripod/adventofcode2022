# Read each line of txt file
file = open("input.txt", "r")
array_of_calories, tmp_calories = [], 0


for line in file:
    if line != "\n":
        tmp_calories += int(line)
    else:
        array_of_calories.append(tmp_calories)
        tmp_calories = 0
# handle last line

array_of_calories.sort(reverse=True)
most_calories_from_3_elf = array_of_calories[0] + array_of_calories[1] + array_of_calories[2]
print(f'The elf with most calories have => {most_calories_from_3_elf}')