def longest_substring_with_k_distinct(str1, k):
    start = 0
    max_length = 0
    char_frequency = {}

    for end in range(len(str1)):
        right_char = str1[end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        #print(char_frequency)

        # shrink the sliding window, until we are left with 'k' distinct characters
        #   in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[start]
            #print(left_char)
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            start += 1 # shrink the window
        # remember maximum length so far

        print(char_frequency)
        max_length = max(max_length, end-start+1)
        print(max_length)
    return max_length

print("Longest substring length: " + str(longest_substring_with_k_distinct('araaci',2)))
print("Longest substring length: " + str(longest_substring_with_k_distinct('araaci',1)))
print("Longest substring length: " + str(longest_substring_with_k_distinct('cbbebi',3)))

