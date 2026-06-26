#lc2. 两数相加，
# https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-100-liked

# wc测试commit

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy=ListNode(-1)
        # temp=dummy
        # jinwei=False
        # while l1 is not None and l2 is not None:
        #     if jinwei:
        #         sum=l1.val+l2.val+1
        #         if sum<10:
        #             temp.next=ListNode(sum)
        #             jinwei=False
        #         if sum>=10:
        #             temp.next=ListNode(sum-10)
        #             jinwei=True
        #     else:
        #         sum=l1.val+l2.val
        #         if sum<10:
        #             temp.next=ListNode(sum)
        #             jinwei=False
        #         if sum>=10:
        #             temp.next=ListNode(sum-10)
        #             jinwei=True

        #     l1=l1.next
        #     l2=l2.next
        #     temp=temp.next

        # while l1:
        #     if jinwei:
        #         sum=l1.val+1
        #         if sum<10:
        #             temp.next=ListNode(sum)
        #             jinwei=False
        #         if sum>=10:
        #             temp.next=ListNode(sum-10)
        #             jinwei=True
        #     else:
        #         sum=l1.val
        #         if sum<10:
        #             temp.next=ListNode(sum)
        #             jinwei=False
        #         if sum>=10:
        #             temp.next=ListNode(sum-10)
        #             jinwei=True
        #     l1=l1.next
        #     temp=temp.next

        # while l2:
        #     if jinwei:
        #         sum=l2.val+1
        #         if sum<10:
        #             temp.next=ListNode(sum)
        #             jinwei=False
        #         if sum>=10:
        #             temp.next=ListNode(sum-10)
        #             jinwei=True
        #     else:
        #         sum=l2.val
        #         if sum<10:
        #             temp.next=ListNode(sum)
        #             jinwei=False
        #         if sum>=10:
        #             temp.next=ListNode(sum-10)
        #             jinwei=True
        #     l2=l2.next
        #     temp=temp.next

        # if jinwei:
        #     temp.next=ListNode(1)

        # return dummy.next



        # 创建哑节点方便处理
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # 遍历两个链表，直到都为空且没有进位
        while l1 or l2 or carry:
            # 获取当前节点的值，如果链表已经为空则取0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算和与新的进位
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # 创建新节点
            current.next = ListNode(digit)
            current = current.next
            
            # 移动指针
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

