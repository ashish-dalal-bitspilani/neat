from collections import Counter


def min_window_substring(s:str, t:str) -> str:

    # check for edge cases
    # s has shorter length than t
    if len(s) < len(t):
        return ""

    # s has the same length as t
    if len(s) == len(t):
        return s if Counter(s) == Counter(t) else ""

    # set of t is not subset of set of s
    if not(set(t).issubset(set(s))):
        return ""

    left, right, window_map, target_map = 0, 0, {}, Counter(t)
    answer = (float("inf"), None, None)

    while right < len(s):
        pass

    return "" if answer[0] == float("inf") else s[answer[1]:answer[2]+1]