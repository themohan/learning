class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def add_first(self, val):
        node =  Node(val)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            node.next = self.start
            self.start = node
        self.size += 1

    def add_last(self, val):
        node = Node(val)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
        self.size += 1

    def remove_first(self):
        if self.start is None:
            return -1
        val = self.start.val
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next
        self.size -= 1
        return val

    def remove_last(self):
        if self.start is None:
            return -1
        if self.start == self.end:
            val = self.start.val
            self.start = None
            self.end = None
            self.size -= 1
            return val

        curr = self.start
        while curr.next != self.end:
            curr = curr.next
        val = self.end.val
        curr.next = None
        self.end = curr
        self.size -= 1
        return val

    def print_list(self):
        curr = self.start
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.start
        for _ in range(index):
            curr = curr.next
        return curr.val

    def contains(self, value):
        curr = self.start
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

# testing
if __name__ == "__main__":
    ll = LinkedList()

    ll.add_last(10)
    ll.add_last(20)
    ll.add_first(5)

    ll.print_list()

    print("Removed First:", ll.remove_first())
    print("Removed Last:", ll.remove_last())

    ll.print_list()
    print("Contains 10?", ll.contains(10))
    print("Size:", ll.get_size())

