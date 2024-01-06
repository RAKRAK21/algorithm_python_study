import itertools

L, C = map(int, input().split())
characters = input().split(" ")
characters.sort()


vowel = ['a', 'e', 'i', 'o', 'u']
password = []

if C == 3:
    print(*characters, sep="")
else:
    vowel_char = [] 
    consonant_char = []
    for char in characters:
        if char in vowel:
            vowel_char.append(char)
        else:
            consonant_char.append(char)
    
    if len(vowel_char) > L-2:
        for vowel_count in range(1, L-1):
            vowel_comb = list(itertools.combinations(vowel_char, vowel_count))
            consonant_comb = list(itertools.combinations(consonant_char, (L-vowel_count)))
            for vowels in vowel_comb:
                for consonants in consonant_comb:
                    val = list(vowels+consonants)
                    val.sort()
                    password.append("".join(val))
                    
    else:
        for vowel_count in range(1, len(vowel_char)+1):
            vowel_comb = list(itertools.combinations(vowel_char, vowel_count))
            consonant_comb = list(itertools.combinations(consonant_char, (L-vowel_count)))
            for vowels in vowel_comb:
                for consonants in consonant_comb:
                    val = list(vowels+consonants)
                    val.sort()
                    password.append("".join(val))

    password.sort()
    for value in password:
        print(value)
            