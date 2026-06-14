# lc116， 填充每个节点的下一个右侧节点指针
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        if root.left is None:
            return root
        root.left.next=root.right
        #root.right.next=None  因为 root.right 可能有右侧邻居：不能这么写
        if root.next:  # 只有父节点有 next 时，才设置右孩子的 next  
        #"之所以这里能判断父节点是不是有next，是因为上次迭代中已经给父节点的next赋值了"
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        #labuladon，只关注当前迭代的节点，别的不要管，不要想太多一层一层处理的。
        
        return root
