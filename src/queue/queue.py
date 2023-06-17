from listQueue import *
from ListStack import *

#2번
def check_same(s) -> bool:
    word = ListQueue()
    sign_index=0
    for c in s:
        sign_index+=1
        if c=='$': break
        word.enqueue(c)
    
    for i in range(sign_index, len(s)):
        if (s[i]!=word.dequeue()): return False

    return True

print("="*10,"2번","="*10)
print(check_same("123$123"))
print(check_same("123$321"))
print()

#4번
class qtostack:
    def __init__(self):
        self.q1 = ListQueue()
        self.q2 = ListQueue()

    def move(self, q1:ListQueue, q2:ListQueue):
        while not q1.isEmpty():
            q2.enqueue(q1.dequeue())

    def push(self, element):
        self.move(self.q1, self.q2)
        self.q1.enqueue(element)
        self.move(self.q2, self.q1)

    def pop(self):
        return self.q1.dequeue()

print("="*10,"4번","="*10)
qs = qtostack()
for i in range(5):
    qs.push(i)
for i in range(5):
    print(qs.pop())
print()

#4번 변형문제
class qtostack_revised:
    def __init__(self):
        self.q1 = ListQueue()
        self.q2 = ListQueue()

    def move(self, q1:ListQueue, q2:ListQueue):
        while len(q1.queue)>0: #1개 남을 때 까지
            q2.enqueue(q1.dequeue())

    def push(self, element):
        self.q1.enqueue(element)

    def pop(self):
        self.move(self.q1, self.q2)
        self.q1, self.q2 = self.q2, self.q1 #나머지 요소 swap 해주기
        return self.q1.dequeue()

print("="*10,"4번 변형","="*10)
qsr = qtostack_revised()
for i in range(5):
    qs.push(i)
for i in range(5):
    print(qs.pop())
print()

#5번
class stacktoq:
    def __init__(self):
        self.s1 = ListStack()
        self.s2 = ListStack()
    
    def move(self, s1:ListStack, s2:ListStack):
        while not s1.isEmpty():
            s2.push(s1.pop())

    def enqueue(self, element):
        self.move(self.s1, self.s2)
        self.s1.push(element)
        self.move(self.s2, self.s1)
    
    def dequeue(self):
        return self.s1.pop()

print("="*10,"5번","="*10)
sq = stacktoq()
for i in range(5):
    sq.enqueue(i)
for i in range(5):
    print(sq.dequeue())