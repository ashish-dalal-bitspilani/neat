# s = "ashish is a developer.ashish is appearing in an interview."

from collections import defaultdict

def longest_repeating_substring(string:str)->(str, int):
    left, right, counter, max_len, result = 0, 0, defaultdict(int), -1, ""
    for left in range(len(string)):
        for right in range(left+1, len(string)+1):
            substring = string[left:right]
            counter[substring] +=  1
            length = right - left

            if max_len < length and counter[substring] > 1:
                max_len, result = length, substring

    return result, max_len



print(longest_repeating_substring(string = "ashish is a developer.ashish is appearing in an interview."))