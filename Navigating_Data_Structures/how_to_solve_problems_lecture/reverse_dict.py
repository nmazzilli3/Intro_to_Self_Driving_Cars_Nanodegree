def reverse_dictionary(dictionary):
    new_d = {}
    # TODO - your code here
    for key in dictionary:
        value = dictionary[key]
        new_d[value] = key
    return new_d

eng_to_spa = {
    "red" :    "rojo",
    "blue"   : "azul",
    "green"  : "verde",
    "black"  : "negro",
    "white"  : "blanco",
    "yellow" : "amarillo",
    "orange" : "naranja",
    "pink"   : "rosa",
    "purple" : "morado",
    "gray"   : "gris"
}

# TESTING CODE

spa_to_eng = reverse_dictionary(eng_to_spa)
print('English to Spanish')
print(eng_to_spa)
print()
print('Spanish to English')
print(spa_to_eng)
assert(len(spa_to_eng) == len(eng_to_spa))
assert(spa_to_eng['rojo'] == 'red')
assert(spa_to_eng['azul'] == 'blue')
assert(spa_to_eng['verde'] == 'green')

print("Nice work! Your reverse_dictionary function is correct.")

#Spanish to French 

def spanish_to_french_2(english_to_spanish, english_to_french):
    """
    Given an English to Spanish dictionary and an English
    to French dictionary, returns a Spanish to French dictionary.
    
    If any words appear in one dictionary but NOT the other, 
    they
	"""

    s2f = {}
    for english_word in english_to_french:
        if english_word in english_to_spanish:
            french_word = english_to_french[english_word]
            spanish_word = english_to_spanish[english_word]
            s2f[spanish_word] = french_word
    return s2f

french_to_eng = {
    "bleu"  : "blue",
    "noir"  : "black", 
    "vert"  : "green",
    "violet": "purple",
    "gris"  : "gray",
    "rouge" : "red",
    "orange": "orange",
    "rose"  : "pink",
    "marron": "brown",
    "jaune" : "yellow",
    "blanc" : "white",
}
english_to_french = reverse_dictionary(french_to_eng)

S2F_2 = spanish_to_french_2(eng_to_spa, english_to_french)
print()
print(S2F_2)

"""
Dictionary Summary
Important things to remember about dictionaries!

1. Dictionaries associate keys with values
The following dictionary has 2 keys ("abc" and "def") and 2 values (123 and 456)

d = {"abc":123, "def":456}
2. Dictionaries are Unordered
Two dictionaries are identical if they have the same keys and those keys are associated with the same values. Order doesn't matter.

> d1 = {"abc":123, "def":456}
> d2 = {"def":456, "abc":123}
> d1 == d2
True
3. Dictionaries are "mutable"
This means they can be modified in various ways

3.1 adding new elements
> d = {}
> d['k'] = 'v'
> print(d)
{'k': 'v'}
3.2 removing elements
> del d['k']
> print(d)
{}
3.3 changing elements
> d['key'] = 'value' # first need to add an element back in
> print(d)
{'key': 'value'}

> d['key'] = 'other value'
> print(d)
{'key' : 'other value'}
4. Looping through a dictionary
When looping through a dictionary, you loop through the keys of that dictionary.

5. Membership Testing
Python's in keyword can be used to test if something is a key in a dictionary.

"""