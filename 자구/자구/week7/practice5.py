from stack.listStack import ListStack

st1 = ListStack()

def parenBalance(s) -> bool: 
    for i in (s):
        if (i =='('):
            st1.push(i)
        
        elif (i ==')'):
            if st1.isEmpty(): #닫는 괄호가 더 많을 경우, list가 비어있어서 예외 처리
                print("괄호의 좌우 균형이 맞지 않습니다(닫는 기호가 더 많음)")
                return False
            else:
                st1.pop()


    if st1.isEmpty():
        print("괄호의 좌우 균형이 맞습니다")
        return True
    else:
        print("괄호의 좌우 균형이 맞지 않습니다(여는 기호가 더 많음)")
        return False


checking = input("문자열을 입력하세요: ")
parenBalance(checking)

