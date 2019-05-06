# python code for quick sort
import random

arr = [random.randint(0, 100) for i in range(25)]
def quick_sort(arr, l, h):
    if l<h:
        par = partition(arr, l, h)
        quick_sort(arr, l,par-1)
        quick_sort(arr, par+1, h)

def partition(arr, l, h):
    piv = arr[h]
    i = l-1
    for j in range(l, h):
        if arr[j] <= piv:
            i+=1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i+1]
    arr[i+1] = arr[h]
    arr[h] = temp
    return i+1
      
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)
