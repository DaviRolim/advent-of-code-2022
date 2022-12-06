# To pass solution 1 just change fourteen and (14) to four and (4)
# A nice improvement would be to use a queue so I don't have to pop from position zero and rearrange the list with every iteration.
# find the index of the first occurrence of four consecultives non repeating characters in a string
def find_first_non_repeating_four_char_index(input_string):
    # recent_four = list(input_string[0:4])
    recent_fourteen = list(input_string[0:14])
    # print(recent_four)
    # loop through the rest ot the string
    for i in range(14, len(input_string)):
        if input_string[i] in recent_fourteen or len(set(recent_fourteen)) < 14:
            recent_fourteen.append(input_string[i])
            recent_fourteen.pop(0)
            print(recent_fourteen)
        else:
            return i


with open("input.txt", "r") as f:
    input_string = f.read()
    input_string = input_string.strip()
    index = find_first_non_repeating_four_char_index(input_string)
    print(index)