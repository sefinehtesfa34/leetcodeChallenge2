# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.l=[]
        self.lists=lists
        for i in self.lists:
            head=i
            temp=i
            while temp:
                self.l.append(temp.val)
                temp=temp.next
        self.l.sort()
        self.l=self.l[::-1]
        head=None
        for i in self.l:
            node=ListNode(i)
            node.next=head
            head=node
        return head
            
                
