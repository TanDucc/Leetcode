def myPow(x: float, n: int) -> float:
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = helper(x * x, n // 2)
        return x * res if n % 2 else res
    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res

# Example usage:
x = 2.0
n = 10
result = myPow(x, n)
print(result)  # Output: 1024.0

# Tính myPow(2, 10)
        # 2^10 = (2^2)^5 = 4^5
        # 4^5 = 4 * (4^2)^2 = 4 * (16^2)
        # 16^2 = (16^2) = (256^1)
        # 256^1 = 256 * (256^0) = 256 * 1
    