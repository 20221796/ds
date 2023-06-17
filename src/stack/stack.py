from ListStack import *
# from LinkedListBasic import *

def parenBalance(s) -> bool:
    paren = ListStack()

    for c in s: 
        if c=='(':
            paren.push(c)
        elif c==')':
            if paren.isEmpty():
                return False
            paren.pop()

    return True

print(parenBalance("((800/ (3+5)*2), (82+2)/4), (91*(40-35)+2)"))

def check_reverse(s) -> bool:
    word = ListStack()
    sign_index=0
    for c in s:
        sign_index+=1
        if c=='$': break
        word.push(c)
    
    for i in range(sign_index, len(s)):
        if (s[i]==word.pop()): return True

    return False

print(check_reverse("hi$ih"))

def evaluate(expresion):
    tmp = ListStack()
    operator = ['+', '-', '*', '/']
    num = ""
    prevdigit = False
    for element in expresion:
        if element == ' ' and prevdigit:
            tmp.push(int(num))
            num = ""
        elif element.isdigit():
            num += element
            prevdigit = True
        elif element in operator:
            tmp.push(operation(tmp.pop(), tmp.pop(), element))
            prevdigit = False
    return tmp.pop()

def operation(b, a, ch):
    return {'+':a+b, '-':a-b, '*':a*b, '/':a//b}[ch]

postfix = "700 3 47 + 6 * - 4 /"
print("input: ", postfix)
answer = evaluate(postfix)
print("answer: ", answer)
