# Time complexity : O(s2)
# Space complexity : O(s1)

from collections import Counter
def check_inclusion(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    window = len(s1)
    target_counter = Counter(s1)
    current_counter = Counter(s2[:window])

    for i in range(len(s2) - window + 1):
        if current_counter == target_counter:
            return True
        if i < len(s2) - window:
            current_counter[s2[i]] -= 1
            if current_counter[s2[i]] == 0:
                del current_counter[s2[i]]
            current_counter[s2[i + window]] = current_counter.get(s2[i + window], 0) + 1

    return False

print(check_inclusion(s1 = "abc", s2 = "lecabee"))
print(check_inclusion(s1 = "abc", s2 = "lecaabee"))