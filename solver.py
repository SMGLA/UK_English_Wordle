# Wordle Solver Program

from title import solver_title

import pprint

# TODO: Create a word list from a word_data.file
with open("word_data.txt") as file:
    word_data = file.readlines()
    word_list = [word.strip('\n') for word in word_data]

    # TODO: Create a dictionary of each word: character dictionary and store them in a list
    word_char_dict_list = []
    for word in word_list:
        index_char_dict = {i: char for i, char in enumerate(word)}  # {0: 'o', 1: 't', 2: 'r', 3: 'o', 4: 's'}
        word_dict = {word: index_char_dict}
        word_char_dict_list.append(word_dict)

# pprint.pprint(word_char_dict_list) # [{'ellos': {0: 'e', 1: 'l', 2: 'l', 3: 'o', 4: 's'}}, {'tener': {0: 't', 1: 'e', 2: 'n', 3: 'e', 4: 'r'}}, ...

print(solver_title)
# TODO: Ask how many characters in the correct position the used has found
try:
    num_char_green_found = int(input("How many characters in the correct position have you found? (🟩 only): "))
except ValueError:
    print("Please enter a number")

found_number_green_list = []
char_found_green_list = []
char_found_position_list = []

for i in range(1, num_char_green_found + 1):
    if i == 1:
        nth_word = "1st"
        found_number_green_list.append(nth_word)
    elif i == 2:
        nth_word = "2nd"
        found_number_green_list.append(nth_word)
    elif i == 3:
        nth_word = "3rd"
        found_number_green_list.append(nth_word)
    elif i == 4:
        nth_word = "4th"
        found_number_green_list.append(nth_word)

for current_nth_green_word in found_number_green_list:
    char_found = input(f"What is the {current_nth_green_word} character?: ")
    # is_valid = True
    # while is_valid:
    #     if not char_found.isalpha():
    #         print("Please enter a number")
    char_found_green_list.append(char_found)
    char_found_position = input(f"What is the position of the {current_nth_green_word} character? (1st > 1): ")
    char_found_position_list.append(int(char_found_position) - 1)

# TODO: Create dictionary of the user input (found characters and their position)
char_found_dict = char_found_green_list = {index: char for index, char in zip(char_found_position_list, char_found_green_list)}
# print(char_found_dict) # {0: 'p', 1: 'u'}

# TODO: Check the words in the word list to see if the user input matches and add the word to the possible list
check_result = []
possible_word_green_list = []

for word_char_dict in word_char_dict_list:
    check_result = []
    # print(word_char_dict_list)  # [{'ellos': {0: 'e', 1: 'l', 2: 'l', 3: 'o', 4: 's'}}, {'tener': {0: 't', 1: 'e', 2: 'n', 3: 'e', 4: 'r'}}, ....
    # print(word_char_dict)  # {'ellos': {0: 'e', 1: 'l', 2: 'l', 3: 'o', 4: 's'}}
    for (word_char_dict_key, word_char_dict_value) in word_char_dict.items():
        # print(word_char_dict_key)  # ellos
        # print(word_char_dict_value)  #  {0: 'e', 1: 'l', 2: 'l', 3: 'o', 4: 's'}
        for char_found_dict_key, char_found_dict_value in char_found_dict.items():
            # print(char_found_dict_key)  # 0
            # print(char_found_dict_value)  # t
            if char_found_dict_key in word_char_dict_value and char_found_dict_value == word_char_dict_value[char_found_dict_key]:
                check_result.append("Pass")
            else:
                check_result.append("Fail")
    # print(check_result)  # ['Fail', 'Pass']
    if all(result == "Pass" for result in check_result):
        # print("Pass")
        possible_word_green_list.append(word_char_dict_key)

# TODO: Ask how many characters in the incorrect position the used has found
print("")
num_char_yellow_found = int(input("How many characters in the incorrect position have you found? (🟨️ only): "))

found_number_yellow_list = []
char_found_yellow_list = []

for i in range(0, num_char_yellow_found + 1):
    if i == 0:
        found_number_yellow_list = []
    elif i == 1:
        nth_word = "1st"
        found_number_yellow_list.append(nth_word)
    elif i == 2:
        nth_word = "2nd"
        found_number_yellow_list.append(nth_word)
    elif i == 3:
        nth_word = "3rd"
        found_number_yellow_list.append(nth_word)
    elif i == 4:
        nth_word = "4th"
        found_number_yellow_list.append(nth_word)

for current_nth_yellow_word in found_number_yellow_list:
    char_found_yellow = input(f"What is the {current_nth_yellow_word} character?: ")
    char_found_yellow_list.append(char_found_yellow)

possible_word_interim_list = []

for possible_word in possible_word_green_list:
    if len(char_found_yellow_list) == 0:
        possible_word_interim_list = possible_word_green_list[:]
    else:
        check_list = []
        for char_yellow in char_found_yellow_list:
            if char_yellow in possible_word:
                # print(char_yellow)
                # print(possible_word)
                check_list.append(True)
            else:
                check_list.append(False)
        # print(len(set(check_list)))
        if len(set(check_list)) == 1 and check_list[0] == True:
            possible_word_interim_list.append(possible_word)
    check_list = []

# TODO: Ask how many of unused characters in the word were found
print("")
num_char_black_found = int(input("How many of unused characters in the word have you found? (⬛️ only): "))

found_number_black_list = []
char_found_black_list = []

for i in range(0, num_char_black_found + 1):
    if i == 0:
        found_number_black_list = []
    elif i == 1:
        nth_word = "1st"
        found_number_black_list.append(nth_word)
    elif i == 2:
        nth_word = "2nd"
        found_number_black_list.append(nth_word)
    elif i == 3:
        nth_word = "3rd"
        found_number_black_list.append(nth_word)
    elif i >= 4:
        nth_word = f"{i}th"
        found_number_black_list.append(nth_word)

for current_nth_black_word in found_number_black_list:
    char_found_black = input(f"What is the {current_nth_black_word} character?: ")
    char_found_black_list.append(char_found_black)

# print(char_found_black_list)

possible_word_final_list = []

for interim_word in possible_word_interim_list:
    for char_black in char_found_black_list:
        if char_black not in interim_word:
            possible_word_final_list.append(interim_word)

print("")
print("The answer could be:")

for possible_answer in sorted(set(possible_word_final_list)):
    print(possible_answer)
