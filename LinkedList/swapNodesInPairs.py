# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        counter=0
        l=[]
        while temp:
            l.append(temp.val)
            counter+=1
            if counter==2:
                pop1=l.pop()
                pop2=l.pop()
                l.extend([pop1,pop2])
                counter=0
            temp=temp.next
        l=l[::-1]
        head=None
        for i in l:
            node=ListNode(i)
            node.next=head
            head=node
        return head
                
            
        
