# Time complexity : O(n)
# Space complexity : O(n)
def isPalindrome(s: str) -> bool:
    if len(s) in [0, 1]:
        return True

    text = [t.lower() for t in s if t.isalnum()]
    return text == text[::-1]

print("===========================================")
print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("tab a cat"))
print("===========================================")

# Time complexity : O(n)
# Space complexity : O(1)
def checkPalindrome(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        if s[left].isalnum() and s[right].isalnum() and s[left].lower() != s[right].lower():
            return False
        elif not(s[left].isalnum()):
            left += 1
        elif not(s[right].isalnum()):
            right -= 1
        else:
            left += 1
            right -= 1
    return True

print("===========================================")
print(checkPalindrome("Was it a car or a cat I saw?"))
print(checkPalindrome("tab a cat"))
print("===========================================")