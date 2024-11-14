def find_non_decreasing_subsequences(nums):
    result = []
    
    def backtrack(start, path):
        if len(path) > 1:
            result.append(path[:])  # Add a copy of the current path to the result

        for i in range(start, len(nums)):
            if not path or nums[i] >= path[-1]:  # Check non-decreasing condition
                path.append(nums[i])  # Include nums[i] in the subsequence
                backtrack(i + 1, path)  # Move to the next index
                path.pop()  # Backtrack to explore other possibilities

    backtrack(0, [])
    return result

# Example usage
input_array = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]
non_decreasing_subsequences = find_non_decreasing_subsequences(input_array)
print(input_array)
print(non_decreasing_subsequences)