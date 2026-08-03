from collections import deque
from typing import List

def maxResult(nums: List[int], k: int) -> int:
    n = len(nums)
    dequeList = deque([0])  # Lưu các chỉ số, đảm bảo giá trị nums[index] giảm dần

    for i in range(1, n):
        # Cộng điểm lớn nhất có thể nhảy tới vị trí i (chỉ số đầu deque luôn là điểm tốt nhất trong phạm vi k)
        nums[i] += nums[dequeList[0]]

        # Loại bỏ các chỉ số ở cuối deque mà giá trị tại đó nhỏ hơn hoặc bằng nums[i]
        while dequeList and nums[i] >= nums[dequeList[-1]]:
            dequeList.pop()
        # Thêm chỉ số i vào cuối deque
        dequeList.append(i)
        # Nếu chỉ số đầu deque đã vượt quá phạm vi k bước, loại bỏ khỏi deque
        if dequeList[0] == i - k:
            dequeList.popleft()
    return nums[-1]  # Trả về điểm lớn nhất tại vị trí cuối cùng

# Example usage:
nums = [10, -5, -2, 4, 0, 3]
k = 3
result = maxResult(nums, k)
print(result)  # Output: 17