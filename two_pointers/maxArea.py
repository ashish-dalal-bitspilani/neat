# Time complexity : O(n)
# Space complexity : O(1)
def maxArea(heights: list[int]) -> int:

    left, right = 0, len(heights) - 1
    area = 0

    while right > left:
        breadth = right - left
        length = min(heights[left], heights[right])
        area = max(area, breadth * length)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return area

print(maxArea([1,7,2,5,4,7,3,6]))
print(maxArea([2,2,2]))