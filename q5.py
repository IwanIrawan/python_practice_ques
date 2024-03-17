# Write a Python function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string.

# For example:

# count_vowels("hello") should return 2 because there are two vowels ('e' and 'o') in the word "hello".
# count_vowels("python") should return 1 because there is one vowel ('o') in the word "python".
# count_vowels("apple") should return 2 because there are two vowels ('a' and 'e') in the word "apple".
# Your function should be case insensitive, meaning it should treat uppercase and lowercase vowels as the same.

# Note: You can assume that the input string only contains alphabetic characters (no punctuation or digits).

def count_vowel(a: str) -> int:
    count = 0
    for char in a:
        if char in 'aeiou' or char in 'AEIOU':
            count += 1
    return count

a = 'pnuemonoultramicroscopicsilicovolcanocoliosis'
print(count_vowel(a))