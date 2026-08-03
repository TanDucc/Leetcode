from collections import defaultdict
from collections import Counter

def frequencySort(self, s: str) -> str:
    count = Counter(s)
    buckets = defaultdict(list)
    
    for char, cnt in count.items():
        buckets[cnt].append(char)
    res = []
    
    for i in range(len(s), 0, -1):
        for c in buckets[i]:
            res.append(c * i)
    return ''.join(res)

# Example usage:
s = "tree"
result = frequencySort(None, s)
print(result)  