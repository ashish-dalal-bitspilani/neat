# Time Complexity : O(n^2)
# Space Complexity : O(n)

def product(nums: list[int]) -> int:
    if not len(nums) or 0 in nums:
        return 0

    product = 1

    for num in nums:
        product *= num

    return product

def productExceptSelf(nums: list[int]) -> list[int]:
    product_arr = []
    for index in range(len(nums)):
        arr = nums[:index] + nums[index + 1:]
        product_arr.append(product(arr))
    return product_arr

print(productExceptSelf(nums = [1,2,4,6]))
print(productExceptSelf(nums = [-1,0,1,2,3]))

# Time Complexity : O(n)
# Space Complexity : O(n)

def product_except_self(nums: list[int]) -> list[int]:
    length, left, right = len(nums), 1, 1
    result = [1]*length

    for index in range(length):
        result[index] = left
        left *= nums[index]

    for index in range(length-1, -1, -1):
        result[index] *= right
        right *= nums[index]

    return result

print(product_except_self(nums = [1,2,4,6]))
print(product_except_self(nums = [-1,0,1,2,3]))
