# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        l=l[::-1]
        head=None
        for i in l:
            node=ListNode(i)
            node.next=head
            head=node
        return head
