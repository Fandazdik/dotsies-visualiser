from numpy import array
import random
import math

dot_dict = {'a': 16,
 'b': 8,
 'c': 4,
 'd': 2,
 'e': 1,
 'f': 24,
 'g': 12,
 'h': 6,
 'i': 3,
 'j': 20,
 'k': 10,
 'l': 5,
 'm': 18,
 'n': 9,
 'o': 17,
 'p': 28,
 'q': 26,
 'r': 22,
 's': 14,
 't': 13,
 'u': 11,
 'v': 7,
 'w': 25,
 'x': 21,
 'y': 19,
 'z': 27,
 ' ': 0}


array_to_display = []


def pad(text, amount):
    return '0' * (amount - len(text)) + text

def to_list(letter):
    global dot_dict
    
    int_list = []
    
    binary = bin(dot_dict[letter.lower()])
    binary = binary[2:]
    binary = pad(binary, 5)[::1]
    
    for i in range(len(binary)):
        #print(binary[i])
        int_list.append(int(binary[i]))
    
    return list(binary)

# def show(letter):
#     final_list = []
#     list_to_print = to_list(letter)
#     for item in list_to_print:
#         if item == 0:
#             print('-')
#         if item == 1:
#             print('#')

string = 'test'
def string_to_array(string, char_tup = ('░░', '██')):
    array_to_display = []
    disp_string = ''
    for char in string:
        array_to_display.append(to_list(char))
        

    final_array = array(array_to_display)
    final_array = final_array.swapaxes(0, 1)

    for list_item in final_array:

        for char in list_item.tolist():
            if char == '0':
                disp_string += char_tup[0]
            elif char == '1':
                disp_string += char_tup[1]
        disp_string += '\n'
    return disp_string

# length = 1
# while 1:
#     letter_type = 1
#     #REPLACE LETTER TYPE BELOW
#     possible_letters = patterns[0] + patterns[1]
#     chosen_letters = ''
#     for i in range(math.floor(length)):
#         chosen_letters += random.choice(possible_letters)
#     #print(chosen_letter)
#     print(string_to_array(chosen_letters, ('░░', '██')))
#     guess = input('> ')
#     print()
#     if guess.lower() == chosen_letters:
#         print('Correct')
#         length += 0.05
#     else:
#         print(f'Incorrect, answer was {chosen_letters}')
    