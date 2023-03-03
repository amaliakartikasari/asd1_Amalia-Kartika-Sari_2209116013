import os
from random import randint
os.system("cls")

print("""
Nama    : Amalia Kartika Sari
NIM     : 2209116013
""")
inilist = [randint(0,50) for i in range(10)]
def quicksort(inilist):
    if len(inilist) <= 1:
        return inilist
    else:

        pivot = inilist[0]

        left = [x for x in inilist[1:] if x <= pivot]

        right = [x for x in inilist[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    
def shellsort(inilist):
    n = len(inilist)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = inilist[i]
            j = i

            while j >= gap and inilist[j - gap] > temp:
                inilist[j] = inilist[j - gap]
                j -= gap

            inilist[j] = temp
        gap //= 2

    return inilist

print(f"unsorted : {inilist}")
print(65*'=')
result = quicksort(inilist)
hasil = shellsort(inilist)
print (f'sorted by shellsort : {hasil}')
print(65*'=')
print (f'sorted by quicksort : {result}')
print(65*'=')