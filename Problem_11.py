# Write a pythnon program to find the gien string are Anagram Or Not

def check(s1, s2):
    if sorted(s1) == sorted(s2):
        print('The strings are anagrams.')
    else:
        print('The strings are not anagrams.')

s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
check(s1, s2)



