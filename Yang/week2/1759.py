# 1759. 암호 만들기
from itertools import combinations

VOWEL = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
characters = [x for x in input().split()]
vowel = []
for element in characters :
    if element in VOWEL :
        vowel.append(element)
vowel = sorted(vowel)
consonant = sorted(list(set(characters) - set(vowel)))
answer = []
for i in range(len(vowel)) :
    # len(consonant) > 1
    if l-i-1 > 1 :
        for vowels in combinations(vowel, i+1) :
            for consonants in combinations(consonant, l-i-1) :
                answer.append(sorted(list(vowels + consonants)))
