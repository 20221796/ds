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
    
    B = sorted(B.items(), key = lambda x: x[1],reverse=True)

    for i in range(10):
        print(B[i])



if __name__ == "__main__":
    sort_count("실습\linkbench_short.trc")