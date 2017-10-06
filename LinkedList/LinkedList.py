
#Implements a singly linked list
class Node():
    def __init__(self,data,nextNode):
        self.__data = data
        self.__nextNode = nextNode

    def getData(self):
        return self.__data

    def getNextNode(self):
        return self.__nextNode

    def setNextNode(self, Node):
        self.__nextNode = Node




class LinkedList():
    def __init__(self):
        self.head = Node(None,None)
        self.size = 0


    def getSize(self):
        return self.size

    def insert(self, data):
        pointer = self.head
        while(True):
            if(not pointer.getNextNode()):
                pointer.setNextNode(Node(data,None))
                self.size += 1
                break

            pointer = pointer.getNextNode()
        

    #Check test case -- not found    
    def delete(self):
        #Deletes the first node in the list
        nodeToDelete = self.head.getNextNode()
        connectToHead = nodeToDelete.getNextNode()
        self.head.setNextNode(connectToHead)
        self.size -= 1


     #Check test case -- not found    
    def deleteNodeWithDataOf(self, data):
        currentNode = self.head
        
        while(True):
            ##Fix this method************
            currentNode = currentNode.getNextNode()
            nextNode = currentNode.getNextNode()
            
            if (currentNode.getData() == data):
                self.head.setNextNode(nextNode)#to delete at first node in list
                self.size -= 1
                print("Deleted")#Garbage collector will delete object
                break

            #Excludes the item from the list, if found
            elif (nextNode != None and nextNode.getData() == data):
                currentNode.setNextNode(nextNode.getNextNode())
                self.size -= 1
                break
            
            elif(not currentNode.getNextNode()):
                print("Not found")
                break



    
    def display(self):
        pointer = self.head
        
        while(True):
            
            pointer = pointer.getNextNode()
            print(pointer.getData())
            
            if(not pointer.getNextNode()):
                break


            
            
    def search(self, data):
        pointer = self.head
        
        while(True):
            
            pointer = pointer.getNextNode()

            if (pointer.getData() == data):
                print("found")
                break
            
            elif(not pointer.getNextNode()):
                print("Not found")
                break

