# 543. 二叉树的直径
# https://leetcode.cn/problems/diameter-of-binary-tree/description/

# 方法一：实例方法
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxDepth(root)
        return self.diameter
    
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        
        # 更新直径
        self.diameter = max(self.diameter, left_depth + right_depth)
        
        # 返回深度
        return max(left_depth, right_depth) + 1
    
# 方法一：嵌套方法
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0#也可写在maxDepth(root)前面
        
        def maxDepth(node):  # 嵌套函数
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        
        #self.diameter = 0
        maxDepth(root)
        return self.diameter