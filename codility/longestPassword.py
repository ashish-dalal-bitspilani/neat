class Solution:

    def __init__(self, problem):
        self.problem = problem

    @staticmethod
    def longest_password(s: str)-> int:
        passwords = []
        strings = s.split()
        for string in strings:
            if not string.isalnum():
                continue
            digit_count, alphabet_count = 0, 0
            for element in string:
                if element.isdigit():
                    digit_count += 1
                if element.isalpha():
                    alphabet_count += 1
            if alphabet_count % 2 == 0 and digit_count % 2 != 0:
                passwords.append(string)
        return len(max(passwords, key=len)) if len(passwords) > 0 else -1


if __name__ == "__main__":
    solution = Solution("longestPassword")
    print(solution.longest_password("test 5 a0A pass007 ?xy1"))