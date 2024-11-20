s = "My name is ashish dalal."
target_output = ["ashish", "dalal", "is", "My", "name"]
words = s.split()
print(sorted(words, key = lambda x : x[0].lower()))