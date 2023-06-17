A = [{1:1},{2:1},{3:1}]

for node, i in zip(A, range(3)):
    node[i+1] += 1

print(A)