class Solution:

    def __init__(self, problem):
        self.problem = problem

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        if len(nums) in [0, 1]:
            return []

        indices = {}

        for index in range(len(nums)):
            try:
                return sorted([index, indices[target - nums[index]]])
            except KeyError:
                indices[nums[index]] = index

if __name__ == "__main__":
    solution = Solution("twoSum")
    print(solution.twoSum(nums = [3,4,5,6], target = 7))
    print(solution.twoSum(nums = [4,5,6], target = 10))