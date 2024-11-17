from collections import Counter
# Time Complexity : O(s+t)
# Space Complexity : O(s+t)

def isAnagram_1(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print("===========================================")
print(isAnagram_1(s = "racecar", t = "carrace"))
print(isAnagram_1(s = "jar", t = "jam"))
print("===========================================")

# Time Complexity : O(s+t)
# Space Complexity : O(s+t)

def isAnagram_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    if len(s) == len(t) and len(s) == 0:
        return True

    freq_s, freq_t = {}, {}

    for element in s:
        if element not in t:
            return False
        else:
            freq_s[element] = freq_s.get(element, 0) + 1

    for element in t:
        if element not in s:
            return False
        else:
            freq_t[element] = freq_t.get(element, 0) + 1

    for element in s:
        if freq_s[element] != freq_t[element]:
            return False

    return True

print("===========================================")
print(isAnagram_2(s = "racecar", t = "carrace"))
print(isAnagram_2(s = "jar", t = "jam"))
print("===========================================")