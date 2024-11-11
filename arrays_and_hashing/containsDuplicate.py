# Time Complexity : O(n)
# Space Complexity : O(n)
def containsDuplicate(nums: list[int])-> bool:
    return len(nums) != len(set(nums))

# Time Complexity : O(n)
# Space Complexity : O(n)
def checksDuplicate(nums: list[int])-> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time Complexity : O(n)
# Space Complexity : O(n)
def hasDuplicate(nums: list[int])->bool:
    hash_map = dict(zip(nums, range(len(nums))))
    return list(hash_map.values()) != list(range(len(nums)))

# Time Complexity : O(n)
# Space Complexity : O(n)
from collections import Counter
def haveDuplicates(nums: list[int])->bool:
    hash_map = Counter(nums)
    return list(hash_map.values()) != [1]*len(nums)

# Time Complexity : O(n*log(n))
# Space Complexity : O(1) or O(n)
def existDuplicate(nums: list[int])-> bool:
    nums.sort()
    for index in range(1, len(nums)):
        if nums[index] == nums[index-1]:
            return True
    return False

print("===========================================")
print(containsDuplicate(nums = [1, 2, 3, 3]))
print(containsDuplicate(nums = [1, 2, 3, 4]))

print("===========================================")
print(checksDuplicate(nums=[1, 2, 3, 3]))
print(checksDuplicate(nums=[1, 2, 3, 4]))

print("===========================================")
print(hasDuplicate(nums=[1, 2, 3, 3]))
print(hasDuplicate(nums=[1, 2, 3, 4]))
print("===========================================")

print(haveDuplicates(nums=[1, 2, 3, 3]))
print(haveDuplicates(nums=[1, 2, 3, 4]))
print("===========================================")

print(existDuplicate(nums=[1, 2, 3, 3]))
print(existDuplicate(nums=[1, 2, 3, 4]))
print("===========================================")