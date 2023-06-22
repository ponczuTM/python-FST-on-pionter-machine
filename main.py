import mroczkowski_library as mo
import os
os.system("cls")

"""
#uzycie funkcji sortowania babelkowego
array=[2,6,12,53425,765,876,346,2354,12365345,67467]
mo.bsort(array)
print(array)
"""

"""
#uzycie funkcji z parametrem "show", w tym przypadku dla sortowania babelkowego
mo.bsort(array, "show")
"""

"""
#uzycie funkcji zamieniajacej tablice na drzewo binarne
array=[50, 25, 75, 16, 37, 68, 89, 96, 78, 73, 53, 47, 29, 22, 7]
mo.array_to_tree()
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


array_from_tree = mo.save_binary_tree_to_array(root)
#print(array_from_tree)
#mo.display_tree(root)

#mo.insertion_sort_pointer(array)
#print(array, "\n")
#mo.FST(root, "show")
mo.FST(root)
print("--------------------")
