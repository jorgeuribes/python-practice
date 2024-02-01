#66
'''
ADIVINA LA PALABRA
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
'''

import random
import math
from dict import spanish_words

def pick_word():
    '''
    Function select a word form dic, and replaace <= 60% of the word,
    :return: full-word, mask-word list, list with hidden letters, word length and  number of mask-characters
    '''
    new_word = []
    hidden_letters = []
    my_word = random.choice(spanish_words)
    l = len(my_word)
    l60 = math.ceil(l * .60)
    chances = l - l60
    hidden_positions = random.sample(range(0,l),chances)
    hidden_positions.sort()

    for i in range(0,l):
        if i in hidden_positions:
            new_word.append("_")
            hidden_letters.append(my_word[i])
        else:
            new_word.append(my_word[i])

    return (my_word,new_word,hidden_letters,l,l60)
def ask_entry(num_charts):
    '''
    The function ask the user to type a character or word and validates that it is a valid entry
    :param num_charts: the lenght of the word
    :return: what user typed in
    '''
    invalid_entry = True
    while invalid_entry:
        user_entry = input(f"type in a character missing in the word, or the full word ({num_charts} in lentgth) :")
        if len(user_entry) == 1 or len(user_entry) == num_charts:
            invalid_entry = False
            return (user_entry.lower())
        else:
            print("invalid entry ......")

# get word
full_word, mask_word, missing_letters, word_len, word_len60 = pick_word()
# set variables for ending the game
#lives = word_len - word_len60
# set lives equals to the distinct missing letters
#print(missing_letters)
lives = len(set(missing_letters))
guess_word = False


while lives > 0 and not guess_word:
    print(f"You have {lives} chances to guess the word: {''.join(mask_word)}")
    user_response = ask_entry(len(full_word))
    if len(user_response) == 1 and user_response in missing_letters:
        word_index = 0
        for letter in full_word:
            if user_response == full_word[word_index]:
                mask_word[word_index] = letter
            word_index += 1
            if "_" not in mask_word:
                guess_word = True
    elif user_response == full_word:
        guess_word = True
    else:
        lives -= 1
    print("------------------------------------------------------")
if guess_word:
    print(f"You have won!! you guessed the word {full_word}")
else:
    print(f"You lost, the word was: {full_word}")




