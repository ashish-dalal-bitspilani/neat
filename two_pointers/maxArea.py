class Solution:

    def __init__(self, problem):
        self.problem = problem

    def maxArea(self, heights: list[int]) -> int:
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


if __name__ == "__main__":
    solution = Solution("maxArea")
    print(solution.maxArea([1,7,2,5,4,7,3,6]))
    print(solution.maxArea([2,2,2]))