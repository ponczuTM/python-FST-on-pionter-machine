import mroczkowski_library.functions as mo

"""
mo.sort(arr, "test")
print()
mo.sort(arr, "show")
"""
root = None
root = mo.insert(root, 50)
root = mo.insert(root, 25)
root = mo.insert(root, 75)
root = mo.insert(root, 16)
root = mo.insert(root, 37)
root = mo.insert(root, 68)
root = mo.insert(root, 89)
root = mo.insert(root, 96)
root = mo.insert(root, 78)
root = mo.insert(root, 73)
root = mo.insert(root, 53)
root = mo.insert(root, 47)
root = mo.insert(root, 29)
root = mo.insert(root, 22)
root = mo.insert(root, 7)

#mo.add_standard_edges()

mo.display_tree(root)
print()
array = [5, 2, 35656546, 4, 1, 3, 3, 12, 123, 135, 546, 456]

sorted_arr = mo.bsort(array)
print(sorted_arr, "\n")

mo.insertion_sort_pointer(array)
print(array, "\n")