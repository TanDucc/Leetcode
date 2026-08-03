from typing import List

def longestWord(words: List[str]) -> str:
    words.sort()
    built = set()
    res = ""
    
    for w in words:
        if len(w) == 1 or w[:-1] in built:
            built.add(w)
            if len(w) > len(res):
                res = w
    return res

# Example usage:
words = ["w","wo","wor","worl","world"]
print(longestWord(words))  # Output: "world"
