# Time complexity : O(n*k)
# Space complexity : O(n)
from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

    result = []
    for left in range(len(nums) - k + 1):
        result.append(max(nums[left:left+k]))

    return result

print("===============================================")
print(sliding_window_maximum(nums = [1,2,1,0,4,2,6], k = 3))
print(sliding_window_maximum(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(sliding_window_maximum(nums = [1], k = 1))
print("===============================================")


# Time complexity : O(n*k)
# Space complexity : O(n)

def sliding_window_max(nums: list[int], k: int) -> list[int]:

    if not nums or k == 0:
        return []

    d_queue, result = deque(), []

    for i in range(len(nums)-k+1):

        # Remove indices that are out of the current window
        if d_queue and d_queue[0] < i:
            d_queue.popleft()

        # Remove indices of elements smaller than the current element
        while d_queue and nums[d_queue[-1]] < nums[i]:
            d_queue.pop()

        # Add the current index to the deque
        d_queue.append(i)
        print(f"iteration : {i+1}, dqueue : {d_queue}")
        # Add the maximum element of the window to the result
        # The window is valid only after we've processed at least k elements
        if i >= k - 1 and i+k-1 < len(nums):
            result.append(nums[d_queue[0]])

    return result
print("===============================================")
print(sliding_window_max(nums=[1, 2, 1, 0, 4, 2, 6], k=3))
print(sliding_window_max(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(sliding_window_max(nums=[1], k=1))
print("===============================================")