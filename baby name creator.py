import random,string
#5 separate letters for 5 separate values
def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    letter6 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3+letter4+letter5+letter6
    return (name)

print(generator())

#ask user for input

letter_input_1 = input('choose a letter .."v" for vowels,"c" for consonants,"o" for any other letters')
letter_input_2 = input('choose a letter .."v" for vowels,"c" for consonants,"o" for any other letters')
letter_input_3 = input('choose a letter .."v" for vowels,"c" for consonants,"o" for any other letters')
letter_input_4 = input('choose a letter .."v" for vowels,"c" for consonants,"o" for any other letters')
letter_input_5 = input('choose a letter .."v" for vowels,"c" for consonants,"o" for any other letters')
letter_input_6 = input('choose a letter .."v" for vowels,"c" for consonants,"o" for any other letters')

#now make a condition

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

def generator():
    if letter_input_1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input_1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input_1 == "o":
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1  # the specific letter given

    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input_2 == "o":
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2  # the specific letter given

    if letter_input_3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "o":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3  # the specific letter given

    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "o":
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4  # the specific letter given

    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "o":
        letter5 = random.choice(letter)
    else:
        letter5 = letter_input_5  # the specific letter given

    if letter_input_6 == "v":
        letter6 = random.choice(vowels)
    elif letter_input_6 == "c":
        letter6 = random.choice(consonants)
    elif letter_input_6 == "o":
        letter6 = random.choice(letter)
    else:
        letter6 = letter_input_6  # the specific letter given
    name = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    return (name)

for babynames in range(20):
    print(generator())

