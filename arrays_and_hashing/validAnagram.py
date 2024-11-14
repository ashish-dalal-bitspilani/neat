from collections import Counter

class Solution:

    def __init__(self, problem):
        self.problem = problem

    def isAnagram_1(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


    def isAnagram_2(self, s: str, t: str) -> bool:
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

if __name__ == "__main__":

    solution = Solution("validAnagram")

    print("===========================================")
    print(solution.isAnagram_1(s = "racecar", t = "carrace"))
    print(solution.isAnagram_1(s = "jar", t = "jam"))

    print("===========================================")
    print(solution.isAnagram_2(s = "racecar", t = "carrace"))
    print(solution.isAnagram_2(s = "jar", t = "jam"))

    print("===========================================")