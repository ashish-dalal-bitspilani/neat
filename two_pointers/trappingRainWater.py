class Solution:

    def __init__(self, problem):
        self.problem = problem

    def trap(self, heights:list[int])->int:
        left, right = 0, len(heights)-1
        left_max, right_max = heights[left], heights[right]

        water = 0

        while right > left:
            if right_max > left_max:
                left += 1
                left_max = max(left_max, heights[left])
                water += min(left_max - heights[left], right_max)
                print(f"water level : {water}, left max : {left_max}, right max : {right_max}")
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                water += min(left_max, right_max-heights[right])
                print(f"water level : {water}, left max : {left_max}, right max : {right_max}")
        return water

if __name__ == "__main__":
    solution = Solution("trappingRainWater")
    print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
