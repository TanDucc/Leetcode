def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    maxFre = 0
    
    for  r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxFre = max(maxFre, count[s[r]])
        while (r - l + 1) - maxFre > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

s = "AABABBA"
k = 1
result = characterReplacement(s, k)
print(result) 