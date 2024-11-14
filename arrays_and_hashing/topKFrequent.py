from collections import Counter

def topKFrequent_1(nums: list[int], k: int) -> list[int]:
    return [a for (a,b) in Counter(nums).most_common(k)]

def topKFrequent_2(nums: list[int], k: int) -> list[int]:
    nums_freq_map = {}

    for num in nums:
        nums_freq_map[num] = nums_freq_map.get(num, 0) + 1

    frequencies = set(nums_freq_map.values())
    frequencies = sorted(frequencies, reverse=True)
    top_k = frequencies[:k]

    counter = 0
    most_frequent = []
    while counter < k and len(most_frequent) < k:
        elements = [k for (k, v) in nums_freq_map.items() if v == top_k[counter]]
        most_frequent.extend(elements)
        counter += 1

    return most_frequent

print("===========================================")
print(topKFrequent_1(nums=[7,7], k=1))
print(topKFrequent_1(nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k = 10))
print(topKFrequent_1(nums = [1,2,2,3,3,3], k = 2))
print("===========================================")
print("===========================================")
print(topKFrequent_2(nums=[1, 2, 2, 3, 3, 3], k=2))
print(topKFrequent_2(nums=[7, 7], k=1))
print(topKFrequent_2(nums=[3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], k=10))
print("===========================================")