# element can occur or remain in the array at most k times

# Time Complexity: O(n)
# Space Complexity: O(1)
def threshold_duplicates_sorted_array(nums: list[int], k=2)-> list[int]:
    # either the list is empty or each element can occur at most 0 times
    # which means the element should be non-existent
    if not nums or k == 0:
        return []

    # iterate using left and valid pointer positions, left for the array and valid for final result
    left, valid = 1, 1
    while left < len(nums):
        # if valid position is yet to reach k, we can add as is, no need to check duplicates
        if valid < k:
            nums[valid] = nums[left]
            left += 1
            valid += 1
        # once we have filled up k elements, need to check if left is not equal to previous left
        # if not, that means, we have come across a new number on left
        elif nums[left] != nums[left-1]:
            nums[valid] = nums[left]
            left += 1
            valid += 1
        # if the numbers on the left and previous left are same, then we need to check if entry at k positions behind matches with left or not
        # we move ahead with adding this left entry only if entry at k positions behind is different
        elif nums[left] != nums[valid-k]:
            nums[valid] = nums[left]
            left += 1
            valid += 1
        # if nothing of the above, move forward
        else:
            left += 1

    return nums[:valid]

print(threshold_duplicates_sorted_array(nums=[1,2,2,2,3,4,5,5,6,7,7,7], k=2))



# Time Complexity: O(n)
# Space Complexity: O(1)
def removing_duplicates_sorted_array(nums: list[int], k=2)-> list[int]:
    # either the list is empty or each element can occur at most 0 times
    # which means the element should be non-existent
    if not nums or k == 0:
        return []

    # since the first element is valid anyway, we start seeking valid elements from index 1
    valid = 1

    for index in range(1, len(nums)):
        # if the current element is the same as previous element, check for core logic to ensure duplicate threshold is met
        if nums[index] == nums[index-1]:
            # until the array has  k elements, it is alright to keep filling up
            # once the valid elements are past k, we need to ensure the current element is not the same as element that is k positions behind
            if valid < k  or nums[index] != nums[valid - k]:
                nums[valid] = nums[index]
                valid += 1
        # otherwise, it is a new number, as it does not match the previous number
        else:
            nums[valid] = nums[index]
            valid += 1

    return nums[:valid]

print(removing_duplicates_sorted_array(nums=[1,2,2,2,3,4,5,5,6,7,7,7], k=2))
