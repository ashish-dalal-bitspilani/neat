# Time Complexity : O(n^2)
# Space Complexity : O(n)

def duplicateStatus(nums:list[int])->bool:
    for index, num in enumerate(nums):
        if index == len(nums) - 1:
            return False
        if num in nums[(index+1):]:
            return True
    return False

print("===========================================")
print(duplicateStatus(nums=[1, 2, 3, 3]))
print(duplicateStatus(nums=[1, 2, 3, 4]))
print("===========================================")

# Time Complexity : O(n)
# Space Complexity : O(n)
def containsDuplicate(nums: list[int])-> bool:
    if len(nums) in [0,1]:
        return False

    return len(nums) != len(set(nums))
print("===========================================")
print(containsDuplicate(nums = [1, 2, 3, 3]))
print(containsDuplicate(nums = [1, 2, 3, 4]))
print("===========================================")


# Time Complexity : O(n)
# Space Complexity : O(n)
def checksDuplicate(nums: list[int])-> bool:
    if len(nums) in [0,1]:
        return False

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print("===========================================")
print(checksDuplicate(nums=[1, 2, 3, 3]))
print(checksDuplicate(nums=[1, 2, 3, 4]))
print("===========================================")


# Time Complexity : O(n)
# Space Complexity : O(n)
def hasDuplicate(nums: list[int])->bool:
    if len(nums) in [0,1]:
        return False

    hash_map = dict(zip(nums, range(len(nums))))
    return list(hash_map.values()) != list(range(len(nums)))
print("===========================================")
print(hasDuplicate(nums=[1, 2, 3, 3]))
print(hasDuplicate(nums=[1, 2, 3, 4]))
print("===========================================")


# Time Complexity : O(n)
# Space Complexity : O(n)
from collections import Counter
def haveDuplicates(nums: list[int])->bool:
    if len(nums) in [0,1]:
        return False
    hash_map = Counter(nums)
    return list(hash_map.values()) != [1]*len(nums)
print("===========================================")
print(haveDuplicates(nums=[1, 2, 3, 3]))
print(haveDuplicates(nums=[1, 2, 3, 4]))
print("===========================================")


# Time Complexity : O(n)
# Space Complexity : O(n)
def detectDuplicates(nums: list[int])->bool:
    if len(nums) in [0,1]:
        return False

    hash_map = Counter(nums)
    return not max(hash_map.values()) > 1
print("===========================================")
print(detectDuplicates(nums=[1, 2, 3, 3]))
print(detectDuplicates(nums=[1, 2, 3, 4]))
print("===========================================")

# Time Complexity : O(n*log(n))
# Space Complexity : O(n)
def existDuplicate(nums: list[int])-> bool:
    if len(nums) in [0,1]:
        return False
    nums.sort()
    for index in range(1, len(nums)):
        if nums[index] == nums[index-1]:
            return True
    return False
print("===========================================")
print(existDuplicate(nums=[1, 2, 3, 3]))
print(existDuplicate(nums=[1, 2, 3, 4]))
print("===========================================")