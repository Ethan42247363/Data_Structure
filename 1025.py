class Node:
    def __init__(self,data=None):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,data):
        if self.head==None:
           self.head=Node(data)
        else:
            currentNode=self.head
            while currentNode.next!=None:
                currentNode=currentNode.next

            nwNode=Node(data)
            nwNode.prev=currentNode
            currentNode.next=nwNode

    def traverse(self):
        if self.head==None:
            print("Error")
        else:
            currentNode=self.head
            while currentNode.next!=None:
                print(currentNode.data,"<->")
                currentNode=currentNode.next
            print(currentNode.data,"<--> End")

    def insert(self,index,nwdata):
        if self.head==None and index==0:
            self.head=Node(nwdata)
        elif self.head==None and index>0:
            print("Error")
        else:
            currentNode=self.head
            prevNode=None
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            if i==index:
                nwNode=Node(nwdata)
                nwNode.next=currentNode
                currentNode.prev=nwNode
                if prevNode==None:
                    self.head=nwNode
                else:
                    prevNode.next=nwNode
                    nwNode.prev=prevNode

                
    def search(self,index):
        currentNode=self.head
        prevNode=None
        i=0
        if self.head==None:
            print("Error")
        else:
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            else:
                print(currentNode.data)

    def delete(self,index):
        if self.head==None:
            print("Error")
        else:
            currentNode=self.head
            prevNode=None
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            else:
                prevNode.next=currentNode.next
                currentNode.next.prev=prevNode
        
    def update(self,index,nwdata):
        if self.head==None:
            print("Error")
        else:
            CurrentNode=self.head
            prevNode=None
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            else:
                currentNode.data==Node(nwdata)