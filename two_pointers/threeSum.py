class Solution:

    def __init__(self, problem):
        self.problem = problem

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) in [0,1,2]:
            return [[]]

        nums.sort()
        triplets = set()
        i = 0

        while i < len(nums) - 2:
            j, k = i + 1, len(nums)-1
            while j < len(nums)-1 and k > j:
                status = nums[i] + nums[j] + nums[k]
                if status == 0:
                    triplets.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif status < 0:
                    j += 1
                else:
                    k -= 1
            i += 1

        return [list(t) for t in triplets]


if __name__ == "__main__":
    solution = Solution("threeSum")
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0, 1, 1]))
    print(solution.threeSum([0, 0, 0]))