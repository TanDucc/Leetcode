def isPalindrome(self, s: str) -> bool:
        newString = ""
        for char in s:
            if char.isalnum():
                newString += char.lower()
        return newString == newString[::-1]        