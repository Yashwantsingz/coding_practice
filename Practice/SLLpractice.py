
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def arrayToList(self, arr):
        # code here
        new_node=Node(arr[0])
        curr=self.head
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            curr.next=new_node
            curr=curr.next

        return self.head.data
s1=Solution()
s1.arrayToList([1,2,3,4,5])
s1.traversal()