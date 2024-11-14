class Solution:

    def __init__(self, problem):
        self.problem = problem

    @staticmethod
    def get_maximum_depth(A) -> int:
        left, right = 0, len(A) - 1
        left_max, right_max = A[left], A[right]
        depths = []
        while right > left:
            if right_max > left_max:
                left += 1
                left_max = max(left_max, A[left])
                depths.append(min(left_max - A[left], right_max))
            else:
                right -= 1
                right_max = max(right_max, A[right])
                depths.append(min(left_max, right_max - A[right]))
        return max(depths) if len(depths) > 0 else 0


if __name__ == "__main__":
    solution = Solution("floodDepth")
    print(solution.get_maximum_depth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))
    print(solution.get_maximum_depth([5,8]))