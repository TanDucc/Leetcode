def maxNumberOfBalloons(text: str) -> int:
    from collections import Counter
    countText = Counter(text)
    balloon = Counter("balloon")
    res = len(text)
    for char in balloon:
        res = min(res, countText[char] // balloon[char])
    return res

# Example usage:
text = "nlaebolko"
print(maxNumberOfBalloons(text))  # Output: 1