from typing import List  # Giúp định nghĩa kiểu dữ liệu List[int]

# Định nghĩa class Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}  # Tạo từ điển để lưu: số -> chỉ số

        # Duyệt từng phần tử trong danh sách nums
        for i, num in enumerate(nums):
            # Kiểm tra nếu phần bù (target - num) đã có trong từ điển
            if target - num in value_index:
                # Nếu có, trả về chỉ số hiện tại và chỉ số đã lưu trước đó
                return [i, value_index[target - num]]

            # Nếu chưa có, thêm số hiện tại vào từ điển
            value_index[num] = i

        # Theo đề bài luôn có 1 đáp án đúng nên không cần trả về gì ngoài vòng lặp

# ---- Chạy thử khi chạy độc lập (không phải khi nộp LeetCode) ----
if __name__ == "__main__":
    solution = Solution()  # Tạo đối tượng từ lớp Solution

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Output:", solution.twoSum(nums1, target1))  # [0, 1]

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("Output:", solution.twoSum(nums2, target2))  # [1, 2]

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("Output:", solution.twoSum(nums3, target3))  # [0, 1]
