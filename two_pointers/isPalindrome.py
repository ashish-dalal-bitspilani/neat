class Solution:

    def __init__(self, problem):
        self.problem = problem

    def isPalindrome(self, s: str) -> bool:

        if len(s) in [0, 1]:
            return True

        text = s.lower()

        text = ''.join(text.split())

        for t in text:
            if not t.isalnum():
                text = text.replace(t, "")
        return text == text[::-1]


if __name__ == "__main__":
    solution = Solution("isPalindrome")
    print(solution.isPalindrome("Was it a car or a cat I saw?"))
    print(solution.isPalindrome("tab a cat"))