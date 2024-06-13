# Exercise2_count_char_in_string
def count_chars(string):
    result = {}
    string = string.lower()
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

word = 'Happiness'
print(count_chars(word))
