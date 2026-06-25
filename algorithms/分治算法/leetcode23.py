# lc23, 合并 K 个升序链表https://leetcode.cn/problems/merge-k-sorted-lists/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # 不能写成if lists is None
            return None
        if len(lists)==1:
            return lists[0]  #这里不能写成lists
        # 分治：两两合并
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
        
