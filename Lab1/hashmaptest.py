def substrings_with_two_unique_chars(s):
    substrings = []
    start = 0
    char_count = {}
    
    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        
        # Shrink the window if more than 2 unique characters
        while len(char_count) > 2:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1
        
        # Check if there are exactly 2 unique characters
        if len(char_count) == 2:
            substrings.append(s[start:end+1])
    
    return substrings

s=input()
print(substrings_with_two_unique_chars(s))