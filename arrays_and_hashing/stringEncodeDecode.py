# Time Complexity : O(L) where L is the total length of the encoded string.
# Space Complexity : O(L)
def encode(strs: list[str]) -> str:
    return ''.join([str(len(string)) + '#' + string for string in strs])

# Time Complexity : O(L) where L is the total length of the encoded string.
# Space Complexity : O(L)
def decode(s: str) -> list[str]:
    strings, index = [], 0

    while index < len(s):
        start = s.find('#', index)
        length = int(s[index:start])
        end = start + 1 + length
        strings.append(s[start+1:end])

        index = end
    return strings

print("===========================================")
print(encode(strs = ["neet","code","love","you"]))
print(decode(encode(strs= ["neet","code","love","you"])))
print(encode(strs = ["we","say",":","yes"]))
print(decode(encode(strs=["we","say",":","yes"])))
print("===========================================")