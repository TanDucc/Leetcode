def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter = {}
    for c in magazine:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for c in ransomNote:
        if c not in counter:
            return False
        elif counter[c] == 1:
            del counter[c]
        else:
            counter[c] -= 1
    return True

#def canConstruct(ransomNote: str, magazine: str) -> bool:
#     from collections import Counter
#     countRansomNote = Counter(ransomNote)
#     countMagazine = Counter(magazine)
#     for c in countRansomNote:
#         if countRansomNote[c] > countMagazine.get(c, 0):
#             return False
#     return True

# Example usage:
ransomNote = "aaa"    
magazine = "aaab"
result = canConstruct(ransomNote, magazine)
print(result)         
                        