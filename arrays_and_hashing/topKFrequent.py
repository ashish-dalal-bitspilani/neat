# Time Complexity : O(n + n*log(n)) because most_common internally sorts based on frequencies of unique elements
# Space Complexity : O(n)
from collections import Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
    return [a for (a,b) in Counter(nums).most_common(k)]

print("===========================================")
print(topKFrequent(nums=[7,7], k=1))
print(topKFrequent(nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k = 10))
print(topKFrequent(nums = [1,2,2,3,3,3], k = 2))
print("===========================================")

# Time Complexity : O(n)
# Space Complexity : O(n)
from collections import defaultdict
def top_k_frequent(nums: list[int], k: int) -> list[int]:

    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    freq_map = defaultdict(list)

    for num in hash_map:
        freq_map[hash_map[num]].append(num)

    frequencies = list(range(len(nums), 0, -1))

    top_k = []

    for freq in frequencies:
        top_k.extend(freq_map[freq][:k - len(top_k)])
        if len(top_k) == k:
            return top_k

    #print(f"hash map : {hash_map}")
    #print(f"freq map : {freq_map}")
    return top_k

print("===========================================")
print(top_k_frequent(nums=[7, 7], k=1))
print(top_k_frequent(nums=[3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k=10))
print(top_k_frequent(nums=[1, 2, 2, 3, 3, 3], k=2))
print("===========================================")