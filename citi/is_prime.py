# Time complexity : O(N)
# Space complexity : O(N)

def is_prime(num: int) -> bool:

    if num in [0,1]:
        return False

    if num == 2:
        return True

    counter = 2

    while counter < num:
        if num % counter == 0:
            return False
        counter += 1
    return True

print(is_prime(9))
print(is_prime(37))

print("=====================================")
# Time complexity : O(N**(1/2))
# Space complexity : O(N**(1/2))
def check_prime(num: int) -> bool:
    if num in [0,1]:
        return False
    if num == 2:
        return True

    counter = 2

    while counter <= num**(0.5):
        if num % counter == 0:
            return False
        counter += 1

    return True

print(check_prime(9))
print(check_prime(37))

print("=====================================")