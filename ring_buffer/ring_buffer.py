from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if about to be full:
        if len(self.storage) == self.capacity - 1:
            # set up for removal of oldest (head will be at first)
            self.current = self.storage.head
            self.storage.add_to_tail(item)
            # print(self.get())
            return

        # if full:
        if len(self.storage) >= self.capacity:

            # if the node we're replacing is the head, update head attribute
            if self.current is self.storage.head:
                # 1) delete the head
                # 2) add to head
                # 3) make head.next oldest
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head.next
                # return

            # if the node we're replacing is the tail, update tail attribute
            elif self.current is self.storage.tail:
                # 1) delete the tail
                # 2) add to tail
                # 3) make head oldest
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
            else:
                # self.current.insert_after(item)
                self.current.value = item
                # temp = self.current.next.next
                # self.storage.delete(self.current)
                self.current = self.current.next

            # NOW HANDLING DELETING IN EACH IF BLOCK
            # below not needed
            # actually remove oldest node
            # self.storage.delete(self.current)

            # if newest item is the tail, change oldest to the head node

        elif self.storage.length < 4:
            self.storage.add_to_tail(item)

        # print(self.get())

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage is not None:
            curr_node = self.storage.head
            list_buffer_contents.append(self.storage.head.value)
            while curr_node.next is not None:
                curr_node = curr_node.next
                list_buffer_contents.append(curr_node.value)

        return list_buffer_contents


new_buff = RingBuffer(5)

new_buff.append('a')
new_buff.append('b')
new_buff.append('c')
new_buff.append('d')
new_buff.append('e')
new_buff.append('f')
new_buff.append('g')
new_buff.append('h')
new_buff.append('i')

print(new_buff.get())


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
