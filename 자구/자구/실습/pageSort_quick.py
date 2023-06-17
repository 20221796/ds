def quickSort2(list) :  
    n = len(list)
    for i in range(n) :
        for j in range(0, n-i-1) :
            if list[j][0] > list[j+1][0] :
                list[j], list[j+1] = list[j+1], list[j]

    list.reverse()

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

    quickSort2(L)
     

    for i in range(10):
        print(L[i][1], L[i][0])



if __name__ == "__main__":
    sort_count("실습\linkbench_short.trc")