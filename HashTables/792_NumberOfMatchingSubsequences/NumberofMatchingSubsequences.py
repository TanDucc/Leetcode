from typing import List
from collections import defaultdict

def numMatchingSubseq(s: str, words: List[str]) -> int:
    lookup = defaultdict(list)  # Tạo dict lưu vị trí xuất hiện của từng ký tự trong s
    output = 0
    for i, c in enumerate(s):
        lookup[c].append(i)  # Lưu tất cả vị trí xuất hiện của ký tự c trong s

    def binarySearch(list, i):
        l, r = 0, len(list)
        while l < r:
            mid = (l + r) // 2
            if i < list[mid]:
                r = mid
            else:
                l = mid + 1            
        return l  # Trả về chỉ số đầu tiên lớn hơn i

    for w in words:
        prev = -1  # Vị trí ký tự trước đó trong s
        found = True  # Biến kiểm tra có phải là subsequence không
        for c in w:
            tmp = binarySearch(lookup[c], prev)  # Tìm vị trí xuất hiện tiếp theo của c sau prev
            if tmp == len(lookup[c]):  # Nếu không tìm thấy
                found = False
                break
            else:
                prev = lookup[c][tmp]  # Cập nhật vị trí prev cho ký tự tiếp theo
        if found:
            output += 1  # Nếu w là subsequence của s thì tăng output
    return output  # Trả về tổng số từ là subsequence

# Example usage
s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(numMatchingSubseq(s, words))  # Output: 3