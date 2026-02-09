class MyLinkedList:

    def __init__(self):
        self.val=None  
        self.next=None

        

    def get(self, index: int) -> int:
        if index<0:
            return -1
        curr=self.next
        count=0
        while curr is not None:
            if count==index:
                return curr.val
            curr=curr.next
            count+=1
        return -1
            

    def addAtHead(self, val: int) -> None:
        new_node=MyLinkedList()
        new_node.val=val
        new_node.next=self.next
        self.next=new_node

    def addAtTail(self, val: int) -> None:
        curr=self
        while curr.next is not None:
            curr=curr.next
        new_node=MyLinkedList()
        new_node.val=val
        curr.next=new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0:
            return
          
        # if index==0:
        #     new_node.next=self.next
        #     self.next=new_node
        #     return
        curr=self
        count=0
        while curr is not None and count<index:#issue with this if index=1 0<1-1(condition false loop will not execute)
            curr=curr.next
            count+=1
        if count==index:
            new_node=MyLinkedList()
            new_node.val=val
    
            new_node.next=curr.next
            curr.next=new_node
        return

        

    def deleteAtIndex(self, index: int) -> None:
        curr=self
        count=0
        if index<0:
            return
        while curr.next is not None and count<index:
            curr=curr.next
            count+=1
        if count==index and curr.next is not None:
            node_to_delete=curr.next
            curr.next=node_to_delete.next
        return

        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
#[[],[1],[3],[1,2],[1],[1],[1]]
s1=MyLinkedList()
# print(s1.addAtHead(1))

print(s1.addAtIndex(0,2))

print(s1.get(0))

print(s1.deleteAtIndex(1))
print(s1.get(1))