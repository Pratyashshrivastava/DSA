from collections import Counter
def minLen(s):
    charCount = Counter(s)
    frequencies = list(charCount.values())
    frequencies.sort(reverse=True)
    removals = 0
    for i in range(min(3,len(frequencies))):
        removals+=frequencies[i]
    return len(s)-removals
s = input()
print(minLen(s))