# COMPREHENSION LIST -- new concept
# https://realpython.com/list-comprehension-python/
squares = [i * i for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# new_list = [expression for member in iterable]
# Every list comprehension in Python includes three elements:
# -expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression i * i is the square of the member value.
# -member is the object or value in the list or iterable. In the example above, the member value is i.
# -iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(10).

sentence = "This is a sample sentence with vowels"
vowels = [i.upper() for i in sentence if i in 'aeiou']
print(vowels)

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]
print(consonants)