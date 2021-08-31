# map function
from random import shuffle

words = ['beetroot', 'carrots', 'potatoes', 'lettuce' ]
anagrams = []

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)

#comprensive method
print([jumble(word) for word in words])

# print(list(map(jumble, words)))


# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)