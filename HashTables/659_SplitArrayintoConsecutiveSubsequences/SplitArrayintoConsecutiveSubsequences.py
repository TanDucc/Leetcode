from typing import List
from collections import Counter
from collections import defaultdict

def isPossible(nums: List[int]) -> bool:
    counter = Counter(nums)  # Đếm số lần xuất hiện của từng số trong mảng
    end = defaultdict(int)   # Lưu số lượng dãy con kết thúc tại một số nhất định
    for num in nums:
        if counter[num] > 0:  # Nếu số này còn chưa dùng hết
            counter[num] -= 1  # Đánh dấu đã dùng số này
            if end[num - 1] > 0:  # Nếu có dãy con kết thúc ở num-1
                end[num - 1] -= 1  # Nối num vào dãy đó, giảm số dãy kết thúc ở num-1
                end[num] += 1      # Tăng số dãy kết thúc ở num
            elif counter[num + 1] > 0 and counter[num + 2] > 0:  # Nếu có thể tạo dãy mới [num, num+1, num+2]
                counter[num + 1] -= 1  # Dùng luôn num+1
                counter[num + 2] -= 1  # Dùng luôn num+2
                end[num + 2] += 1      # Tạo dãy mới kết thúc ở num+2
            else:
                return False  # Không thể nối hoặc tạo dãy mới, trả về False
    return True  # Duyệt hết mà không gặp lỗi, trả về True

input_nums = [1, 2, 3, 3, 4, 4, 5, 5]
print(isPossible(input_nums))  #