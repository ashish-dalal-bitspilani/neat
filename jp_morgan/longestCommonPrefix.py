class Solution:

    def __init__(self, problem):
        self.problem = problem

    def longestCommonPrefix(self, strs:list[str])->str:

        if not strs:
            return ""

        prefix = strs[0]

        for string in strs:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

if __name__ == "__main__":
    solution = Solution("longestCommonPrefix")
    print(solution.longestCommonPrefix(["bog", "boga", "boag"]))