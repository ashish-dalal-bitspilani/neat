# Time Complexity : O(n)
# Space Complexity : O(n)
def longestConsecutive(nums: list[int]) -> int:
    if len(nums) in [0, 1]:
        return len(nums)

    nums, longest_seq = set(nums), 0
    for num in nums:
        if num - 1 not in nums:
            counter = 1
            successor = num + 1
            while successor in nums:
                counter += 1
                successor += 1
            longest_seq = max(longest_seq, counter)

    return longest_seq

print(longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5]))
print(longestConsecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1]))
print(longestConsecutive(nums=[100,4,200,1,3,2]))
print(longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
