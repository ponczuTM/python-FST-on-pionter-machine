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
        self.index += 1
        self.counter += 1
    def go_L(self):
        self.index -= 1
        self.counter += 1
    def go_U(self):
        self.index = self.index - len(self.registers)
        self.counter += 1
    def go_D(self):
        self.index = self.index + len(self.registers)
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
            self.move(finger - self.index)
            self.get()
            if (closest_finger is None or abs(self.value - number) < smallest_distance):
                closest_finger = finger
                smallest_distance = abs(self.value - number)
        self.move(closest_finger - self.index)
        self.get()
        
    def find_FST(self, number):
        self.counter = 0
        steps = 0
        self.get_closest_finger(number)
        while number != self.value:
            self.get()
            if self.value is None:
                print(f"steps in algorithm: {steps}")
                self.move(-self.index)
                return False
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


    def find_BST(self, number):
        self.move(-self.index)
        self.counter = 0
        steps = 0
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

        return True
    
    
    def find_DFS(self, number):
        self.counter = 0
        steps = 0
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

def find(root, type, txt):
    machine = PointerMachine(save_binary_tree_to_array(root))
    if(txt=="No"):
        while True:
            print("--------------------")
            search_number = int(input("enter the number you are looking for: "))
            if search_number == 0:
                break
            if(type=="FST"):
                result = machine.find_FST(search_number)    
            elif(type=="BST"):
                result = machine.find_BST(search_number)    
            elif(type=="DFS"):
                result = machine.find_DFS(search_number)    
            print(f"Pointer Machine operations: {machine.counter}")        
            if result == True:
                print(f"Number {search_number} ✅ found in binary tree") # in vertex {result.val}")
            else:
                print(f"Number {search_number} ❌ NOT found in binary tree")
    elif(txt=="Yes"):
        try:
            filename = input("enter input file name: ")
            # filename = "input.txt" # if you want to run time test, uncomment this line and comment line above
            with open(filename, 'r') as file:
                numbers_from_txt = [int(num.strip()) for num in file.read().split(',')]
            for search_number in numbers_from_txt:
                if search_number == 0:
                    break
                if(type=="FST"):
                    result = machine.find_FST(search_number)    
                elif(type=="BST"):
                    result = machine.find_BST(search_number)    
                elif(type=="DFS"):
                    result = machine.find_DFS(search_number)
                print(f"Pointer Machine operations: {machine.counter}")
                if result == True:
                    print(f"Number {search_number} ✅ found in binary tree")
                else:
                    print(f"Number {search_number} ❌ NOT found in binary tree")

        except FileNotFoundError:
            print("Plik 'input.txt' nie został znaleziony.")
            numbers_from_txt = []

def FST(root, show=None): 
    if show == 'show':
        with open("files/FST_2.txt", "r") as file:
            content = file.read()
            print(content)
    elif show == 'txt_input':
        find(root, "FST", "Yes")
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:
        find(root, "FST", "No")

def BST(root, show=None): 
    if show == 'show':
        with open("files/BST.txt", "r") as file:
            content = file.read()
            print(content)
    elif show == 'txt_input':
        find(root, "BST", "Yes")
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:
        find(root, "BST", "No")

def DFS(root, show=None): 
    if show == 'show':
        with open("files/DFS.txt", "r") as file:
            content = file.read()
            print(content)
    elif show == 'txt_input':
        find(root, "DFS", "Yes")
    elif show is not None:
        print("Invalid argument. Use 'show' to display function.")
    else:
        find(root, "DFS", "No")

def find_tree_depth(node):
    if node is None:
        return 0
    else:
        left_depth = find_tree_depth(node.left)
        right_depth = find_tree_depth(node.right)
        return max(left_depth, right_depth) + 1