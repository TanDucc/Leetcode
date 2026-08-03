def numSplits(s: str) -> int:
    n = len(s)
    prefix = [0] * n
    suffix = [0] * n
    preSet = set()
    sufSet = set()
    
    for i in range(n):
        preSet.add(s[i])
        sufSet.add(s[n - 1 - i])
        prefix[i] = len(preSet)
        suffix[n - 1 - i] = len(sufSet)
    goodWays = 0
    for i in range(1, n):
        if prefix[i - 1] == suffix[i]:
            goodWays += 1
    return goodWays  # Trả về số cách chia chuỗi thành hai

s = "aacaba"
print(numSplits(s))  # Output: 2        