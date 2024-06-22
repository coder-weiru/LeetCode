# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nextA = headA
        nextB = headB
        intersect = None
        map = {}
        while nextA != None:
            map[nextA] = 1
            nextA = nextA.next
        while nextB != None:
            if bool(map.get(nextB)):
                intersect = nextB
                break
            nextB = nextB.next    
        return intersect
        
