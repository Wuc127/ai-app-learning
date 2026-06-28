# lc100,https://leetcode.cn/problems/sort-list/description/?envType=study-plan-v2&envId=top-100-liked

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 下面这么写会超时
        # 快慢指针找中点的方式导致递归树不平衡，
        # 最坏情况下时间复杂度退化为 O(n²)。
        #slow=fast=head
        # while fast is not None and fast.next is not None:
        #     slow=slow.next
        #     fast=fast.next.next
        # temp=slow.next
        # slow.next=None
        # left=self.sortList(head)
        # right=self.sortList(temp)

        slow=fast=head
        prev = None  
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        left=self.sortList(head)
        right=self.sortList(slow)




        return self.mergeTwoLists(left,right)


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1 is not None:
            p.next = p1
        else:
            p.next = p2
        return dummy.next


