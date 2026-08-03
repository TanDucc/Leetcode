def isPalindrome(s: str) -> bool:
    def alphaNum(c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not alphaNum(s[left]):
            left += 1
        while right > left and not alphaNum(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1  
    return True             

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output