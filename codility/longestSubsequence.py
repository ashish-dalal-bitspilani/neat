from pprint import pprint
def longest_increasing_subsequence(A):
    length = len(A)
    if not length:
        return length
    increasing_subsequences = {}

    for index in range(length):
        increasing_subsequences.setdefault(index, [A[index]])
        for sub_index in range(index):
            if A[sub_index] <= A[index]:
                increasing_subsequences[index].insert(0,A[sub_index])
    
    

    pprint(increasing_subsequences)

longest_increasing_subsequence(A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3])