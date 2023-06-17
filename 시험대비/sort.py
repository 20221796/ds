def heapsort(A):
    buildHeap(A)
    for last in range(len(A), 0, -1):
        A[last], A[0] = A[0], A[last]
        percolateDown(A, 0, last-1)

def buildHeap(A):
    for i in range(len(A)-1):
        percolateDown(A,i,len(A)-1)

def percolateDown(A, k, end):
    left = 2*k + 1
    right = 2*k + 2

    if left <= end:
        if right<=end and left < right:
            left = right

        if A[left] > A[k]:
            A[left], A[k] = A[k], A[left]
            percolateDown(A, left, end)


def quicksort(A, left, right):
    if left<right:
        pivot = partition(A, left, right)
        quicksort(A, left, pivot-1)
        quicksort(A, pivot+1, right)

def partition(A, left, right):
    x=A[right]
    i = left-1

    for j in range(left, right):
        if A[j] < x:
            i+= 1
            A[i], A[j] = A[i], A[j]
    
    A[i+1], A[right] = A[right], A[i+1]
    return i+1


def mergesort(A, left, right):
    if left<right:
        pivot = (left+right)/2
        mergesort(A, left, pivot)
        mergesort(A, pivot+1, right)
        merge(A, left, pivot, right)

def merge(A, left, pivot, right):
    i=left; j=pivot+1; t=0
    temp = [0 for i in range(len(A))]
    
    while i<=pivot and j<=right:
        if A[i] <= A[j]:
            temp[t] = A[i]; t+=1; i+=1
        else:
            temp[t] = A[j]; t+=1; j+=1

    while i<=pivot:
        temp[t] = A[i]; t+=1; i+=1
    while j<=right:
        temp[t] = A[j]; t+=1; j+=1

    i=left; t=0