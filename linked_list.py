class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_ending(self, data):
       if self.head is None:
           self.head = Node(data, None)
           return
       # Start iterating the linked list from the head and reach upto the last node
       itr = self.head
       while itr is not None:
           itr = itr.next
           if itr.next is None:
               itr.next = Node(data, None)
               break


    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return        
        itr = self.head
        linked_list_str = ''
        while itr:
            linked_list_str += str(itr.data)+' --> '
            itr = itr.next    
        print(linked_list_str+' None')

if __name__ == '__main__':
    linked_list = LinkedList()
    #linked_list.print()
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(15)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(5)
    linked_list.print()
    linked_list.insert_at_ending(30)
    linked_list.print()



    