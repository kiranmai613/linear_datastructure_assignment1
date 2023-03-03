def first_non_repeated_char(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Iterate through the string to find the first non-repeated character
    for char in string:
        if char_freq[char] == 1:
            return char

    # If no non-repeated character is found, return None
    return None

# Test the function with some sample inputs
string1 = "hello world"
string2 = "aabbccdd"
string3 = "abcdefg"

print(first_non_repeated_char(string1))  # Output: 'h'
print(first_non_repeated_char(string2))  # Output: None
print(first_non_repeated_char(string3))  