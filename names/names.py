import time
from binary_search_tree import BinarySearchTree
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# duplicates = []  # Return the list of duplicates in this data structure

bst = BinarySearchTree("top")
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    bst.insert(name_1)

# bst.for_each(print)


# for name_2 in names_2:
#     # print(name_2)
#     if bst.contains(name_2):
#         print(name_2)
#         duplicates.append(name_2)
#     # if bst.contains(name_2):
#     #     print(name_2)


# STRETCH SOLUTION
duplicates = list(set(names_1).intersection(names_2))

end_time = time.time()
print(f"{len(duplicates)} duplicates: \n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
