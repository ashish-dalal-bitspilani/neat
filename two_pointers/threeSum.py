# Time complexity : O(n^(2))
# Space complexity : O(k) where k is the number of unique triplets

def threeSum(nums: list[int]) -> list[list[int]]:

    if len(nums) in [0,1,2]:
        return [[]]

    nums.sort()
    triplets = []
    i = 0

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue

        left, right = i + 1, len(nums)-1

        while left < right:
            status = nums[i] + nums[left] + nums[right]
            if status == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif status < 0:
                left += 1
            else:
                right -= 1

    return triplets

print("==========================")
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))
print("==========================")