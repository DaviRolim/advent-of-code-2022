def build_char_priority_map():
    char_in_priority_order='abcdefghijklmnopqrstuvwxyz'
    all_chars_in_order = char_in_priority_order + char_in_priority_order.upper()
    priority_map = {}
    for i, char in enumerate(all_chars_in_order):
        priority_map[char] = i + 1

    return priority_map

def find_repeated_item(component1, component2):
    component1 = set(component1)
    component2 = set(component2)
    return list(component1.intersection(component2))[0]

# with open('input.txt', 'r') as file:
#     priority_map = build_char_priority_map()
#     print(priority_map)
#     lines = file.readlines()
#     sum_of_priorities = 0
#     for line in lines:
#         line = line.strip()
#         print(line)
#         component1 = line[:int(len(line)/2)]
#         component2 = line[int(len(line)/2):]
#         repetead_item = find_repeated_item(component1, component2)
#         priority_points = priority_map[repetead_item]
#         sum_of_priorities += priority_points
# # Solution 1
# print(sum_of_priorities)

#Solution 2
with open('input.txt', 'r') as file:
    priority_map = build_char_priority_map()
    print(priority_map)
    lines = file.readlines()
    sum_of_priorities = 0
    current_group_of_bag = []
    for line in lines:
        line = line.strip()
        current_group_of_bag.append(set(line))
        if len(current_group_of_bag) == 3:
            intersection = current_group_of_bag[0].intersection(current_group_of_bag[1].intersection(current_group_of_bag[2]))
            badge = list(intersection)[0]
            print(badge)

            priority_points = priority_map[badge]
            sum_of_priorities += priority_points
            current_group_of_bag = []


print(sum_of_priorities)