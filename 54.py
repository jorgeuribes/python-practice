
#54
'''
EL "LENGUAJE HACKER"
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''

# Dictionary create from chatGPT https://chat.openai.com/share/a3f025f7-8fb9-4032-9fe7-db2dadb23d7f
leet_alphabet = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '|_',
    'm': '|\/|',
    'n': '|\\|',
    'o': '0',
    'p': '|>',
    'q': '(,)',
    'r': '|2',
    's': '$',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\|/',
    'x': '><',
    'y': '`/',
    'z': '2'
}

print(leet_alphabet)

inputword = input("Type a word that would be translated to leet alphabet: ").lower()
#print(inputword)

translated_word = []
for l in inputword:
    #print(l)
    trans_leter = leet_alphabet.get(l)
    translated_word.append(trans_leter)

print(f"The translated word is: {''.join(translated_word)}" )



