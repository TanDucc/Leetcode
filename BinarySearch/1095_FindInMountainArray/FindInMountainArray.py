class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

        
        
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length - 2
        
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m
        
        #Search Left
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            mid = mountainArr.get(m)
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return m
        
        #Search Right
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            mid = mountainArr.get(m)
            if mid < target:
                r = m - 1
            elif mid > target:
                l = m + 1
            else:
                return m
        return -1
# Example usage:
mountainArr = MountainArray([1, 2, 3, 4, 5, 3, 1])
target = 3
solution = Solution()
print(solution.findInMountainArray(target, mountainArr))  # Output: 2