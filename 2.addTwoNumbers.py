#For create ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#Let List to Listnode
def mkList(l):
    pre=ListNode(0)
    temp=pre
    for val in l:
        temp.next=ListNode(val)
        temp=temp.next
    return pre.next
#Solution Start
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre=ListNode(0)
        temp=pre
        carry=0
        while carry or l1 or l2:
            val=0
            val=(l1.val if l1 else 0)+ (l2.val if l2 else 0)+ (carry if carry!=0 else 0)
            carry=0
            if val>=10:
                carry=val//10
                val=val%10
            temp.next=ListNode(val)
            temp=temp.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return pre.next
#Solution End

#Debug Area Start
l1 = mkList([5])
l2 = mkList([5])
l3 = Solution().addTwoNumbers(l1,l2)
#Debug Area End

