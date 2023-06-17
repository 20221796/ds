from stack.linkedStack import LinkedStack

st1 = LinkedStack()

checking = input("문자열을 입력하세요: ")

cnt = 0
check = 0
num = 0

for i in (checking):
    cnt += 1
    if (i == '$'):
        check = cnt

for i in checking:
    num += 1
    if (num < check):
        st1.push(i)
    elif (num > check):
        if st1.isEmpty ==False:
            if (st1.top() == i):
                st1.pop()



if st1.isEmpty()==True:
    print("집합의 원소이다")

else:
    print("집합의 원소가 아니다")