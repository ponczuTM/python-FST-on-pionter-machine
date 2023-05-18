def help(show=None): 
    if show:
        print("nice try but there is no code to print :)")
    elif show is not None:
        print("Invalid argument. Use 'show' to display sorting function.")
    else:
        print("Welcome to mroczkowskioli library!")
        print("every function have argument \"show\" that will print full source code in that function")
        print("e.g. here you executed help(), but you can also execute help(\"show\")")
        print("\nFunctions available in this library:")

def bsort(array, show=None):
    if show == 'show':
        print("#function for bubble sort:")
        print("def sort(array):")
        print("    n = len(array)")
        print("    for i in range(n):")
        print("        for j in range(0, n-i-1):")
        print("            if array[j] > array[j+1]:")
        print("                array[j], array[j+1] = array[j+1], array[j]")
        print("    return array")
    elif show is not None:
        print("Invalid argument. Use 'show' to display sorting function.")
    else:
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

def test(array, *args):
    num_args = len(args)
    if num_args == 0:
        print("Przekazałeś do funkcji tylko tablicę liczb")
    elif num_args == 1 and isinstance(args[0], str):
        print(f"Przekazałeś do funkcji tylko tablicę liczb oraz napis: {args[0]}")
    elif num_args == 2 and all(isinstance(x, str) for x in args):
        print(f"Przekazałeś do funkcji tablicę liczb oraz dwa napisy: {args[0]} i {args[1]}")
    elif num_args == 3 and all(isinstance(x, str) for x in args):
        print(f"Przekazałeś do funkcji tablicę liczb oraz trzy napisy: {args[0]}, {args[1]} i {args[2]}")
    elif num_args == 4 and all(isinstance(x, str) for x in args):
        print(f"Przekazałeś do funkcji tablicę liczb oraz cztery napisy: {args[0]}, {args[1]}, {args[2]} i {args[3]}")


class pointerMachine:
    def __init__(self, array):
        self.array = array
        self.index = 0
        self.value = None
        self.counter = 0
        self.registers = [None] * 4
    def get(self):
        self.value = self.array[self.index]
        self.counter += 1
    def set(self, value):
        self.array[self.index] = value
        self.counter += 1
    def go_R(self):
        self.index = self.index + 1
        self.counter += 1
    def go_L(self):
        self.index = self.index - 1
        self.counter += 1
    def go_U(self):
        self.index = self.index - len(self.registers)
        self.counter += 1
    def go_D(self):
        self.index = self.index + len(self.registers)
        self.counter += 1
    #def is_end(self):
        #return self.index >= len(self.array)

"""
def insertion_sort_last_dir(array):
    machine = last_dirMachine(array)
    for i in range(1, len(array)):
        machine.index = i
        machine.get()
        while machine.index > 0 and machine.array[machine.index-1] > machine.value:
            machine.array[machine.index] = machine.array[machine.index-1]
            machine.go_L()
        machine.array[machine.index] = machine.value
"""

###############################

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def display_tree(node, level=0, label='>'):
    if node is not None:
        display_tree(node.right, level + 1, 'R')
        print(' ' * 4 * level + label + str(node.val))
        display_tree(node.left, level + 1, 'L')

def search_in_tree(root, last_dir, search_number, current):
    if current is None:
        current = root
        last_dir = 1 if current.val > search_number else -1
    parent = None
    steps = 0
    while current is not None:
        if current.val == search_number:
            return (current, last_dir, steps)
        elif current.val < search_number:
            parent = current
            current = current.right
            steps += 1
            #print("right: " + str(current.val))
        else:
            parent = current
            current = current.left
            steps += 1
            print("left: " + str(current.val))

        if parent is not None:
            if parent.val < search_number and last_dir != 1:
                last_dir = 1
                current = parent
                parent = None
                steps += 1
                print("up 1: " + str(current.val))
            elif parent.val > search_number and last_dir != -1:
                last_dir = -1
                current = parent
                parent = None
                steps += 1
                print("up -1: " + str(current.val))
    return (None, last_dir, steps)

"""
            R96   <-   S
        R89
            L78
    R75
            R73
        L68
            L53
>50
            R47
        R37       <-   P
            L29
    L25
            R22
        L16
            L7
"""

"""
def save_binary_tree_to_array(root):
    def preorder_traversal(node):
        if node is None:
            return -1  # Return -1 for non-existent node
        index = len(array) // 3
        # Temporarily store None for left and right indices. We'll fill these in after the recursive calls.
        array.extend([node.val, None, None])
        left_index = preorder_traversal(node.left)
        right_index = preorder_traversal(node.right)
        # Calculate steps from current node to its children
        if left_index != -1:
            array[index * 3 + 1] = (left_index - index) * 3 - 1
        if right_index != -1:
            array[index * 3 + 2] = (right_index - index) * 3 - 2
        return index
    array = []
    preorder_traversal(root)  # Start pre-order traversal
    return array
"""

def save_binary_tree_to_array(root):
    def preorder_traversal(node, parent_index=None):
        if node is None:
            return -1
        index = len(array) // 4
        array.extend([node.val, None, None, None if parent_index is None else (index - parent_index) * 4])
        left_index = preorder_traversal(node.left, index)
        right_index = preorder_traversal(node.right, index)
        if left_index != -1:
            array[index * 4 + 1] = (left_index - index) * 4 - 1
        if right_index != -1:
            array[index * 4 + 2] = (right_index - index) * 4 - 2
        return index
    array = []
    preorder_traversal(root)
    return array



def FST(root, show=None): 
    if show:
        print("nice try but there is no code to print :)")
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:
        #search_number = int(input("enter the number you are looking for: "))
        #pointer = int(input("enter where you want the pointer: "))
        print("--------------------")
        search_number = 96
        pointer = 7
        last_dir = 0
        result, last_dir, steps = search_in_tree(root, last_dir, pointer, None)
        print("--------------------")
        result, last_dir, steps = search_in_tree(root, last_dir, search_number, result)

        
        if result is not None:
            print(f"Number {search_number} found in binary tree") # w wierzchołku o wartości {result.val}")
        else:
            print(f"Number {search_number} NOT found in binary tree")
        print(f"Number of steps: {steps}")