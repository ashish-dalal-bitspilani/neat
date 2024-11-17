# Time complexity : O(n)
# Space complexity : O(1)

def trap(heights:list[int])->int:

    left, right = 0, len(heights)-1
    left_max, right_max = heights[left], heights[right]

    water = 0
    while right > left:
        if right_max > left_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += min(left_max - heights[left], right_max)
            # print(f"water level : {water}, left max : {left_max}, right max : {right_max}")
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += min(left_max, right_max-heights[right])
            # print(f"water level : {water}, left max : {left_max}, right max : {right_max}")
    return water

print(trap([0,2,0,3,1,0,1,3,2,1]))