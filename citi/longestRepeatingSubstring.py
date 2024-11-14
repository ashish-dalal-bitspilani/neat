# s = "ashish is a developer. ashish is appearing in an interview."
# "longest repeating word"
from collections import Counter
def longest_repeating_word(s:str)->int:
    word_counter = dict(Counter(s))
    return max(list(word_counter.keys()), key=len)

def longest_repeating_substring(s:str)->int:
    freq = {}
    freq[tuple(substring, len)] = frequency


try:

except:

finally: