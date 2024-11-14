# Time Complexity : O(n*m*log(m)) where n is the number of strings, m is the average length of each string
# Space Complexity : O(n*m)


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}

    for string in strs:
        word = ''.join(sorted(string))
        if word not in anagrams:
            anagrams[word] = []
        anagrams[word].append(string)

    return list(anagrams.values())

print("===========================================")
print(groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))
print(groupAnagrams(strs=["x"]))
print(groupAnagrams(strs=[""]))
print("===========================================")

# Time Complexity : O(n*m) where n is the number of strings, m is the average length of each string
# Space Complexity : O(n*m)
from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        # Create a character frequency count list (26 letters from 'a' to 'z')
        count = [0] * 26
        for char in word:
            # Increment the count at the position corresponding to the character
            count[ord(char) - ord('a')] += 1
        key = tuple(count)  # Convert the count list to a tuple
        anagrams[key].append(word)  # Use the tuple as a key to group anagrams

    return list(anagrams.values())

print("===========================================")
print(group_anagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))
print(group_anagrams(strs=["x"]))
print(group_anagrams(strs=[""]))
print("===========================================")