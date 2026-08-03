def reverseWords(s: str) -> str:
    arr = s.split()
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return ' '.join(arr)     


s = "the sky is blue"
result = reverseWords(s)
print(result)  