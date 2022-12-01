elves_calories = []

def parse_line_to_number(line):
    return int(line.strip())

with open('input.txt', 'r') as file:
    input_lines = file.readlines()
    elf_calories = 0

    for line in input_lines:
        if line == '\n' or line == '':
            elves_calories.append(elf_calories)
            elf_calories = 0
            continue
        calories = parse_line_to_number(line)
        elf_calories += calories

# Solution 1
print(max(elves_calories))

# Solution 2
sorted_calories = sorted(elves_calories)
sum_of_max_three = sum(sorted_calories[-3:])
print(sum_of_max_three)





        
