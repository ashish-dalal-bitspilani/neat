def twoSum(nums: list[int], target: int) -> list[int]:

    if len(nums) in [0, 1]:
            return []

    indices = {}

    for index in range(len(nums)):
        try:
            return sorted([index, indices[target - nums[index]]])
        except KeyError:
            indices[nums[index]] = index

print("===========================================")
print(twoSum(nums = [3,4,5,6], target = 7))
print(twoSum(nums = [4,5,6], target = 10))
print("===========================================")