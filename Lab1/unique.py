def get_substrings_with_n_distinct_chars(s, K, N):
    # List to store the substrings that satisfy the condition
    result = []
    
    # Edge case: if the string is shorter than K or N is larger than K, return an empty list
    if len(s) < K or N > K:
        return result
    
    # Traverse through all substrings of length K
    print(len(s) - K + 1)
    for i in range(len(s) - K + 1):
        substring = s[i:i + K]
        print(s[i:i + K])
        
        # Get the set of distinct characters in the current substring
        print(set(substring))
        distinct_chars = set(substring)
        
        # If the number of distinct characters is exactly N, add the substring to the result
        if len(distinct_chars) == N:
            result.append(substring)
    
    return result

# Example usage
s = "examplexx"
K = 3
N = 2
substrings = get_substrings_with_n_distinct_chars(s, K, N)
print(substrings)
