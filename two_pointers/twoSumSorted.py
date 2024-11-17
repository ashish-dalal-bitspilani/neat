# Time complexity : O(n)
# Space complexity : O(1)

def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers)-1
    while right > left:
        status = numbers[left] + numbers[right] - target
        if status == 0:
            return [left+1, right+1]
        elif status > 0:
            right -= 1
        else:
            left += 1

print(twoSum([1,2,3,4],3))