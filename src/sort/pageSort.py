from quickSort import *
from mergeSort import *
import sys

sys.setrecursionlimit(10**5)

def do_sort(input_file):
    data_file = open(input_file)
    A = []
    cnt = 0

    for line in data_file.readlines():
        if cnt > 10000: break
        lpn = line.split()[0]
        A.append(lpn)
        cnt+=1

    for i in range(10):
        print(A[i], end=" ")
    print()

    # quickSort(A, 0, len(A)-1)
    # print("quicksort")

    mergeSort(A, 0, len(A)-1)
    print("mergesort")

    for i in range(10):
        print(A[i], end=" ")
    print()

do_sort("src\sort\linkbench.trc")