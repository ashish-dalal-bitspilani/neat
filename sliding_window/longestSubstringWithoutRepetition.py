# Time complexity : O(n^2)
# Space complexity : O(n)

def longestSubstringWithoutRepetition(s: str) -> int:

    if len(s) in [0, 1]:
        return len(s)

    max_length = 0

    for start in range(len(s)-1):
        nxt = start + 1
        while nxt < len(s) - 1 and s[nxt] not in s[start:nxt]:
            nxt += 1
        max_length = max(max_length, len(s[start:nxt]))

    return max_length

print("=============================================")
print(longestSubstringWithoutRepetition(s = "zxyzxyz"))
print(longestSubstringWithoutRepetition(s = "xxxx"))
print("=============================================")

# Time complexity : O(n)
# Space complexity : O(n)
def longest_substring_without_repetition(s:str) -> int:
    characters, left, max_length = set(), 0, 0

    for right in range(len(s)):
        while s[right] in characters:
            characters.remove(s[left])
            left += 1

        characters.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print("=============================================")
print(longestSubstringWithoutRepetition(s = "zxyzxyz"))
print(longestSubstringWithoutRepetition(s = "xxxx"))
print("=============================================")