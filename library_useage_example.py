import mroczkowski_library as mo
mo.help()
import os
os.system("cls")
mo.help()
print("\n")
# using the bubble sort function
array=[2,6,12,53425,765,876,346,2354,12365345,67467]
mo.bsort(array)
print(array)
#using a function with the "show" parameter, in this case for bubble sort
mo.bsort(array, "show")
