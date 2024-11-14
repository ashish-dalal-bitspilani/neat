class Solution:

    def __init__(self, problem):
        self.problem = problem

    def getPermutations(self, string:str) -> list[str]:

        if len(string) in [0,1]:
            return [string]

        perms = set()
        remaining_perms = self.getPermutations(string[1:])

        for position in range(len(string)):
            for p in remaining_perms:
                perm = p[position:] + string[0] + p[:position]
                perms.add(perm)

        return perms


if __name__ == '__main__':
    solution = Solution("checkInclusion")
    print(solution.getPermutations("abc"))
