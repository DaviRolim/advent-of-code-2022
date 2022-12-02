mapped_values_solution_1 = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

mapped_values_solution_2 = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

lose_against = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
wins_against = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}

choice_points = {'rock': 1, 'paper': 2, 'scissors': 3}

def decrypt(encrypted_option):
    return mapped_values_solution_1[encrypted_option]

def translate_encrypted_message(elf_encrypted, my_encrypted):
    elf_choice = decrypt(elf_encrypted)
    match_outcome = mapped_values_solution_2[my_encrypted]
    if match_outcome == 'draw':
        return elf_choice, elf_choice
    if match_outcome == 'win':
        return elf_choice, wins_against[elf_choice]
    if match_outcome == 'lose':
        return  elf_choice, lose_against[elf_choice]



def get_match_points(my_choice, elf_choice):
    result = choice_points[my_choice]
    if my_choice == elf_choice:
        return result + 3

    if elf_choice == lose_against[my_choice]:
        return result + 6

    return result + 0

with open('input.txt', 'r') as file:
    all_matches = file.readlines()
    total_result = 0
    for match in all_matches:
        match = match.strip() # remove \n
        encrypted_player2_choice, encrypted_player1_choice = match.split(' ')

        # solution 1
        # elf_choice = decrypt(encrypted_player2_choice)
        # my_choice = decrypt(encrypted_player1_choice)
        # end solution 1

        # solution 2
        elf_choice, my_choice = translate_encrypted_message(encrypted_player2_choice, encrypted_player1_choice)
        # end solution 2

        result = get_match_points(my_choice, elf_choice)
        total_result += result

print(total_result)

