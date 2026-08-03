from collections import Counter
from typing import List

def topKFrequent(words: List[str], k: int) -> List[str]:
    count = Counter(words)
    
    sortedWords = sorted(count.keys(), key = lambda word: (-count[word], word))
    
    return sortedWords[:k]


# Example usage:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
result = topKFrequent(words, k)
print(result)