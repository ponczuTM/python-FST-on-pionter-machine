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
        with open("files/bsort.txt", "r") as file:
            content = file.read()
            print(content)

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


class PointerMachine:
    def __init__(self, array):
        self.array = array
        self.index = 0
        self.value = None
        self.counter = 0
        self.registers = []
        self.fingers = set()
        self.fingers.add(0)
    def get(self):
        self.value = self.array[self.index]
        self.counter += 1
    def set(self, value):
        self.array[self.index] = value
        self.counter += 1
    def set_finger(self, index):
        self.fingers.add(index)
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
    def is_end(self):
        return self.index >= len(self.array)

    def move(self, steps):
        while steps > 0:
            self.go_R()
            steps -= 1
        while steps < 0:
            self.go_L()
            steps += 1
    
    def get_closest_finger(self, number):
        closest_finger = None
        smallest_distance = None
        for finger in self.fingers:
            # Get finger index in the array
            # self.get_finger(finger)
            # Move to the index
            #print(f"index before: {self.index}")
            self.move(finger - self.index)
            # Get finger value
            self.get()
            #print(f"index: {self.index}, finger: {finger}, value: {self.value}")

            if (closest_finger is None or abs(self.value - number) < smallest_distance):
                closest_finger = finger
                smallest_distance = abs(self.value - number)
        self.move(closest_finger - self.index)
        self.get()
        #print(f"closest finger: {closest_finger}, value: {self.value}")

    def find_FST(self, number):
        self.counter = 0
        steps = 0
        # Find the closest finger
        self.get_closest_finger(number)
        
        while number != self.value:
            self.get()
            if self.value is None:
                print(f"steps in algorithm: {steps}")
                self.move(-self.index)
                return False
            #if self.value == number:
            #    print(f"steps in algorithm: {steps}")
            #    return True

            if number < self.value:
                self.go_R()
                self.get()
                if self.value is None:
                    print(f"steps in algorithm: {steps}")
                    self.move(-self.index)
                    return False
                self.move(self.value)
                self.get()
                steps += 1
                if self.value is not None:
                    self.set_finger(self.index)
            else:
                self.go_R()
                self.go_R()
                self.get()
                if self.value is None:
                    print(f"steps in algorithm: {steps}")
                    self.move(-self.index)
                    return False
                self.move(self.value)
                self.get()
                steps += 1
                if self.value is not None:
                    self.set_finger(self.index)

        print(f"steps in algorithm: {steps}")
        return True
        
        #number - szukana
        #self.value - wskazywana


    def find_BST(self, number):
        self.counter = 0
        steps = 0
        print(self.value) 
        while number != self.value:
            self.get()
            if number < self.value:
                self.go_R()
                self.get()
                if self.value is None:
                    self.move(-self.index)
                    return False
                else:
                    self.move(self.value)
                    self.get()
                    steps += 1
            elif number > self.value:
                self.go_R()
                self.go_R()
                self.get()
                if self.value is None:
                    self.move(-self.index)
                    return False
                else:
                    self.move(self.value)
                    self.get()
                    steps += 1
        print(f"steps in algorithm: {steps}")
        self.move(-self.index)
        self.get()
        return True
    
    
    def find_DFS(self, number):
        self.counter = 0
        steps = 0
        print(self.value) 
        self.get()        
        while number != self.value:
            if self.value == "#":
                self.move(-self.index)
                print(f"steps in algorithm: {steps}")
                return False
            self.go_R()
            self.go_R()
            self.go_R()
            self.go_R()
            self.get()
            steps+=1
        print(f"steps in algorithm: {steps}")
        self.move(-self.index)
        self.get()
        return True
        
        #number - szukana
        #self.value - wskazywana

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


def save_binary_tree_to_array(root):
    def preorder_traversal(node, parent_index=None):
        if node is None:
            return -1
        index = len(array) // 4
        parent = None if parent_index is None else (parent_index - index) * 4 - 3
        array.extend([node.val, None, None, parent])
        left_index = preorder_traversal(node.left, index)
        right_index = preorder_traversal(node.right, index)
        if left_index != -1:
            array[index * 4 + 1] = (left_index - index) * 4 - 1
        if right_index != -1:
            array[index * 4 + 2] = (right_index - index) * 4 - 2
        return index
    array = []
    preorder_traversal(root)
    array.append("#")
    return array

def FST(root, show=None): 
    if show:
        with open("files/FingerSearchTrees.txt", "r") as file:
            content = file.read()
            print(content)
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:

        machine = PointerMachine(save_binary_tree_to_array(root))

        while True:
            print("--------------------")
            search_number = int(input("enter the number you are looking for: "))
            if search_number == 0:
                break
            result = machine.find_FST(search_number)   
            print(f"Pointer Machine operations: {machine.counter}")           
            if result == True:
                print(f"Number {search_number} ✅ found in binary tree") # w wierzchołku o wartości {result.val}")
            else:
                print(f"Number {search_number} ❌ NOT found in binary tree")


def BST(root, show=None): 
    if show:
        with open("files/BinarySearchTrees.txt", "r") as file:
            content = file.read()
            print(content)
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:

        machine = PointerMachine(save_binary_tree_to_array(root))

        while True:
            print("--------------------")
            search_number = int(input("enter the number you are looking for: "))
            if search_number == 0:
                break
            result = machine.find_BST(search_number)    
            print(f"Pointer Machine operations: {machine.counter}")        
            if result == True:
                print(f"Number {search_number} ✅ found in binary tree") # w wierzchołku o wartości {result.val}")
            else:
                print(f"Number {search_number} ❌ NOT found in binary tree")


def DFS(root, show=None): 
    if show:
        with open("files/BinarySearchTrees.txt", "r") as file:
            content = file.read()
            print(content)
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:

        machine = PointerMachine(save_binary_tree_to_array(root))

        while True:
            print("--------------------")
            search_number = int(input("enter the number you are looking for: "))
            if search_number == 0:
                break
            result = machine.find_DFS(search_number)   
            print(f"Pointer Machine operations: {machine.counter}")           
            if result == True:
                print(f"Number {search_number} ✅ found in binary tree") # w wierzchołku o wartości {result.val}")
            else:
                print(f"Number {search_number} ❌ NOT found in binary tree")


"""
            R96
        R89
            L78
    R75
            R73
        L68
            L53
>50
            R47
        R37
            L29
    L25
            R22
        L16
            L7
"""