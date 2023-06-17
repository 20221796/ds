#heapsort
def heapsort(A):
    builheap(A)
    for last in range(len(A)-1, 0, -1):
        percolatedown(A, 0, last-1)

def builheap(A):
    for i in range((len(A)-2)//2, -1, -1):
        percolatedown(A, i, len(A)-1)

def percolatedown(A, k, end):
    child = 2*k + 1
    right = 2*k + 2

    if child <= end:
        if right <= end and A[child] < A[right]:
            child = right
        
        if A[child] > A[k]:
            A[child], A[k] = A[k], A[child]
            percolatedown(A, child, end)

#quicksort
def quicksort(A, left, right):
    middle = partition(A, left, right)
    quicksort(A, left, middle-1)
    quicksort(A, middle+1, right)

def partition(A, left, right):
    pivot = A[right]
    i = left - 1

    for j in range(left, right):
        if A[j] < pivot:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i+1

#mergesort
def mergesort(A, left, right):
    middle = (left+right)//2
    mergesort(left, middle)
    mergesort(middle+1, right)
    merge(A, left, middle, right)

def merge(A, left, middle, right):
    i=left; j=middle+1
    t=0
    temp = [0 for i in range(left, right)]

    while i<=middle and j <= right:
        if A[i] < A[j]:
            temp[t] = A[i]; i+=1; t+=1
        else:
            temp[t] = A[j]; j+=1; t+=1
    
    while i<=middle:
        temp[t] = A[i]; i+=1; t+=1
    
    while j<=right:
        temp[t] = A[j]; j+=1; t+=1
    
    i=left; t=0
    
    while i<=right:
        A[i] = temp[t]; i+=1; t+=1