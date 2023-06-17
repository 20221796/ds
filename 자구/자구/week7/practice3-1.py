from stack.linkedStack import LinkedStack

st1 = LinkedStack()

checking = input("문자열을 입력하세요: ")


for c in checking:
    st1.push(c)
    if (c=="$"):
        break


   




if st1.isEmpty()==True:
    print("집합의 원소이다")

else:
    print("집합의 원소가 아니다")