#양방향 연결 리스트 구현
from bidirectNode import BidirectNode

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def insert(self, i:int, newItem):
        if (i >= 0 and i<= self.__numItems):
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()") #필요 시 에러 처리
        
    def append(self, newItem) -> None:
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1
    
    def pop(self, *args):
        #args는 가변 파라미터. 인자가 없거나 -1이며 마지막 원소를 처리하기 위함. 파이썬 리스트 규칙 만족
        if self.isEmpty():
            return None
        
        #인덱스 i 결정
        if len(args) != 0: #pop(k)과 같이 인자가 있으면 i=k 할당
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        #i번 원소 삭제
        if (i>=0 and i<=self.__numItems -1):
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retItem
        else:
            return None

    def remove(self, x):
        curr = self.__findNode(x)

        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return x
        else:
            return None
        
    def get(self, *args):
        # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만좀
        if self.isEmpty(): return None

        #인덱스 i 결정
        if len(args) != 0: #인자가 있으면 i=k
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1   

        if (i>=0 and i<=self.__numItems-1):
            return self.getNode(i).item
        else:
            return None
    
    def index(self, x) -> int:
        cnt = 0

        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return -1
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def count(self, x) -> int:
        cnt = 0
        
        for element in self:
            if element == x:
                cnt += 1
        return cnt
    
    def extend(self, a):
        for element in a:
            self.append(element)
    
    def copy(self) -> 'CircularDoublyLinkedList':
        a = CircularDoublyLinkedList
        
        for element in self:
            a.append(element)
        return a
    
    def reverse(self) -> None:
        prev = self.__head; curr = prev.next; next = curr.next #0번 노드(head.next)를 curr로 1번 노드(curr.next)를 next로 정함
        self.__head.next = prev.prev; self.__head.prev = curr #head.prev를 맨앞(head.next)로 땡기고,head.next를 맨끝(head.prev)로 보냄
        
        for i in range(self.__numItems):
            curr.next = prev; curr.prev = next #curr(맨뒤)와 head를 연결; next와 curr(맨뒤)를 연결
            prev = curr; curr = next; next = next.next #head curr next를 한 칸 옆으로 옮기고 반복
    
    def sort(self) -> None:
        a = []
        
        for element in self:
            a.append(element)
        
        a.sort()
        self.clear()

        for element in a:
            self.append(element)
    
    def __findNode(self, x) -> BidirectNode:
        curr = self.__head.next #0번 노드

        while curr != self.__head:
            if curr.item == x: return curr
            else: curr = curr.next #노드 한 칸씩 이동
        
        return None
    
    def getNode(self, i:int) -> BidirectNode:
        curr = self.__head
        
        for i in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self) -> None:
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)
    
class CircularDoublyLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1) #더미노드
        self.iterPostion = self.__head.next #0번 노드
        
    def __next__(self):
        if self.iterPostion == self.__head: #순환 끝
            raise StopIteration
        else: #현재 원소를 리턴하고 다음 원소로 이동
            item = self.iterPostion.item
            self.iterPostion = self.iterPostion.next
            return item