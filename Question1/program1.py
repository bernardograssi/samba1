from collections import Counter
def anagram(a, b):
  return Counter(a) == Counter(b)
