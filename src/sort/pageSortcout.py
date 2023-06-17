from cntSort import *		
import sys

sys.setrecursionlimit(10**5)

def do_sort(input_file):
    data_file = open(input_file)
    A = []
    cnt = 1

    for line in data_file.readlines():
        if cnt > 1000: break
        lpn = line.split()[0]
        A.append(lpn)
        cnt+=1

    A_seted = list(set(A))
    A_cnt = []
    
    for element in A_seted:
        tmp = [element, A.count(element)]
        A_cnt.append(tmp)

    quickSort(A_cnt, 0, len(A_cnt)-1)
    # mergeSort(A_cnt, 0, len(A_cnt)-1)
    
    print("메모리 주소  참조 횟수")
    for node in A_cnt:
        print("%10s %10d" % (node[0], node[1]))
    
do_sort("src\sort\linkbench.trc")