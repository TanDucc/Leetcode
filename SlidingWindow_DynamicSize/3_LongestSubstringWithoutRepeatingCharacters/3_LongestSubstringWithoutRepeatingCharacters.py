def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    res = 0
    l = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
# Example usage:
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3        