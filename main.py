# English Wordle Program
# Still in progress -- Currently 'Replay button is not implemented, no attempt limit!

from title import title
import random

# TODO: Create a character list from a character_list.txt file
with open("character_list.txt") as file:
    character_data = file.readlines()
    character_list = [character.strip('\n') for character in character_data]
    # print(character_list)

# TODO: Create a word list from a word_data.file
with open("word_data.txt") as file:
    word_data = file.readlines()
    word_list = [word.strip('\n') for word in word_data]
    # print(word_list)

correct_characters_list = []
incorrect_characters_list = []
leftover_character_list, character_list_copy = [], character_list[:]

is_continue = True
is_answer_valid = True


def check_answer():
    user_current_answer_box_list = []
    user_current_answer_list = []
    if user_input == "exit":
        print(f"The correct answer was '{picked_word}'.")
        print("Good bye!")
        exit()
    # TODO: Check if the user input exists in the list:
    elif len(user_input) > 5 or len(user_input) < 5:
        print("The entered word is not a 5 letter word!")
    elif not user_input.isalpha():
        print("Please type letter only.")
    else:
        # TODO: Check if the user's input matches the answer
        if user_input == picked_word:
            print("Bingo!")
            print(picked_word)
            print("🟩🟩🟩🟩🟩")
            exit()

        # TODO: If not, check if any of the characters and it's position matches to the answer　一部正解
        else:
            for i in user_input_dict:
                # TODO: If the character and the position is correct　文字と位置が正解
                if user_input_dict[i] == picked_word_dict[i]:
                    user_current_answer_list.append(picked_word_dict[i])
                    user_current_answer_box_list.append("🟩")
                # TODO: If the character is wrong　文字が不正解、出現回数が不正解
                elif user_input_dict[i] not in list(picked_word_dict.values()):
                    user_current_answer_list.append("_")
                    user_current_answer_box_list.append("⬛️")
                    incorrect_characters_list.append(user_input_dict[i])
                # TODO: If the character is correct and the position is wrong　文字が正解、位置が不正解
                elif (i in picked_word_dict) in [value for value in picked_word_dict]:  # 文字が不正解
                    # TODO: Count the number of appearance of a character and if it is greater than the number of the picked_word, treat it as invalid
                    if list(user_input).count(user_input_dict[i]) > list(picked_word).count(picked_word_dict[i]):
                        user_current_answer_list.append("_")
                        user_current_answer_box_list.append("⬛")
                    else:
                        user_current_answer_box_list.append("🟨️")
                        user_current_answer_list.append("_")
                        correct_characters_list.append(user_input_dict[i])
                else:
                    incorrect_characters_list.append(user_input_dict[i])

            global user_current_answer
            user_current_answer = "".join(user_current_answer_list)
            print(user_current_answer)
            user_current_answer_box = "".join(user_current_answer_box_list)
            print(user_current_answer_box)
            correct_characters = ", ".join(sorted(set(correct_characters_list)))
            print(f"Known characters: {correct_characters}")
            incorrect_characters = ", ".join(sorted(set(incorrect_characters_list)))
            print(f"Incorrect characters: {incorrect_characters}")
            for incorrect_character in incorrect_characters_list:
                if incorrect_character in character_list_copy:
                    character_list_copy.remove(incorrect_character)
            leftover_characters = ", ".join(sorted(set(character_list_copy)))
            print(f"Characters left over: {leftover_characters}")
            print("")


# TODO: Pick a word, split into characters and store in a list
picked_word = random.choice(word_list)
picked_word_dict = {index: char_word for index, char_word in enumerate(picked_word)}

# TODO: Show the logo with help and current status (Start with _____)
print(title)
print("Type 'exit' to stop the game")
print("")
user_current_answer = "_____"
print(user_current_answer)
print("")

# TODO: Game continues until the user gets the correct answer
while is_continue:

    while is_answer_valid:
        # TODO: Ask the user to enter the 1st guessed Spanish Word
        # print(picked_word)
        user_input = input("Guess a 5 letter word: ").lower()
        print("")

        # TODO: Split the answer word into characters and store in a dictionary
        user_input_dict = {index: char_word for index, char_word in enumerate(user_input)}

        # TODO: Check if the user input exists in the list:
        check_answer()
