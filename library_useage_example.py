import mroczkowski_library as mo
mo.help()
import os
os.system("cls")
mo.help()
print("\n")
#uzycie funkcji sortowania babelkowego
array=[2,6,12,53425,765,876,346,2354,12365345,67467]
mo.bsort(array)
print(array)
#uzycie funkcji z parametrem "show", w tym przypadku dla sortowania babelkowego
mo.bsort(array, "show")