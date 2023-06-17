import sys
sys.setrecursionlimit(10**7)

def quickSort(A, p:int, r:int):
	if p < r:
		q = partition(A, p, r)
		quickSort(A, p, q-1)	
		quickSort(A, q+1, r)
    
    

def partition(A, p:int, r:int) -> int:
	x = A[r][0]					
	i = p-1					
	for j in range(p, r):	
		if A[j][0] < x:
			i += 1
			A[i], A[j] = A[j], A[i]  
	A[i+1], A[r] = A[r], A[i+1]	   
	return i+1



def sort_count(input_file):

    data_file = open(input_file)
    A = []
    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)
    B = {}
    for c in A:
        if c in B:
            pass
        else:
            B[c] = A.count(c)
    
    L = []
    for c in B:
        L.append([B[c], c])


    L = quickSort(L,0, len(L)-1)

    L.reverse()



    for i in range(10):
        print(L[i])



if __name__ == "__main__":
    sort_count("실습\linkbench_short.trc")