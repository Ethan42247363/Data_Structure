class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        
    def add (self,data):     
        if self.head==None: 
           self.head=node(data)
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next= node(data)

    def traverse(self):
        if self.head==None:
            print("NO Data")
        else:
            currentNode = self.head
            while currentNode.next != None:
                print(currentNode.data,"->",end='')
                currentNode=currentNode.next
            print(currentNode.data,"-->END")

    def Search(self , data):
        index = 0
        flag = 0
        currentNode = self.head
        while currentNode.next != None  and  currentNode.data != data:
            index += 1
            currentNode = currentNode.next
            if currentNode.data==data:
                flag = 1

        if currentNode.data==data:
            flag = 1
        return index if flag else -1
    
    def insert(self,index,nwdata):
        currentNode = None
        prevNode = None
        if self.head==None and index ==0:
           self.head=node(nwdata)
        elif self.head == None and index>0:
            print('Error')
        else:
            currentNode = self.head
            prevNode =self.head
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode= currentNode
                currentNode = currentNode.next
            if i==index:
                prevNode.next= node(nwdata)
                prevNode.next.next = currentNode

    def deletion(self,index):
        currentNode=None
        prevNode=None
        if self.head==None:
            print('Error')
        else:
            currentNode=self.head
            prevNode=self.head
            i=0
            if index == 0:
                self.head = currentNode.next
            while i<index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if currentNode==None:
                print('Error')
            else:
                prevNode.next=currentNode.next

    def update(self,index,newdata):
        currentNode=None
        prevNode=None
        if self.head==None:
            print('Error')
        else:
            currentNode=self.head
            prevNode=self.head
            i=0
            while i<index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i<index:
                print('Error')
            elif i==index:
                currentNode.data=newdata

    def count(self,data):
        if self.head==None:
            print('Error')
        else:
            currentNode=self.head
            prevNode=self.head
            i=0
            while currentNode.next!=None:
                if currentNode.data==data:
                    i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if currentNode.next==None:
                if currentNode.data==data:
                    i+=1
            return i

    def add_sort(self, data):
        new_node=node(data)
        
        if self.head==None:
            self.head=new_node
        elif data<self.head.data:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev=None

            while current!=None and current.data<data:
                prev=current
                current=current.next

            prev.next = new_node
            new_node.next = current

if __name__=='__main__':
    ll=Linkedlist( )
    ll.add(16)
    ll.add(4)
    ll.add(7)
    ll.add(9)
    ll.add(2)
    ll.add(5)
    ll.add(9)
    ll.traverse()        #16,4,7,9,2,5,9
    print(ll.Search(4))  #1
    ll.insert(2,18)
    ll.traverse()        #16,4,18,7,9,2,5,9
    ll.deletion(3)
    ll.traverse()        #16,4,18,9,2,5,9
    ll.update(2,20)
    ll.traverse()        #16,4,20,9,2,5,9
    print(ll.count(9))
    gg=Linkedlist( )
    gg.add_sort(4)
    gg.add_sort(7)
    gg.add_sort(2)
    gg.add_sort(5)
    gg.add_sort(1)
    gg.traverse()