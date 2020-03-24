class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)

        # # if left is open
        # if not self.left:
        #     self.left = BinarySearchTree(value)
        #     return
        # # if right is open
        # if not self.right:
        #     self.right = BinarySearchTree(value)
        #     return

        # # if incoming value is bigger than root
        # if value > self.value and self.right is not None:
        #     self.right.insert(value)
        # else:
        #     #  self.value < value:
        #     self.left.insert(value)
        # # else:
        # #     print("Additional handling needed for this case!!")

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if not target:
            return False

        if self.value is target:
            return True
        elif target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # base case
        # if self.value is target:
        #     return True

        # # recursive case for when target is smaller
        # if target < self.value:
        #     # if we reach end w/o finding target
        #     if self.left is None:
        #         return False
        #     # otherwise recurse and keep looking
        #     return self.left.contains(target)

        # # recursive case for when target is larger
        # if target > self.value:
        #     # if we get to end w/o finding target
        #     if self.right is None:
        #         return False
        #     # otherwise recurse
        #     return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # left first

        if self.left is not None:
            self.left.for_each(cb)

        cb(self.value)

        if self.right is not None:
            self.right.for_each(cb)


bst = BinarySearchTree(3)

bst.insert(1)
bst.insert(2)
bst.insert(4)
# below should be 1
print(bst.left.value)
