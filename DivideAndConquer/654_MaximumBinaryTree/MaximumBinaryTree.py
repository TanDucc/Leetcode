from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def construct(left, right):
            if left > right:
                return None
            maxIndex = left
            for i in range(left, right + 1):
                if nums[i] > nums[maxIndex]:
                    maxIndex = i
            root = TreeNode(nums[maxIndex])
            root.left = construct(left, maxIndex - 1)
            root.right = construct(maxIndex + 1, right)
            return root
        return construct(0, len(nums) - 1)
    

       