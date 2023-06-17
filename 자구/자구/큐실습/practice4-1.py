from linkedQueue import LinkedQueue

class TwoQueueStack:
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()
    
    def __move_elements(self, q, tq):  
        while not q.isEmpty():
            tq.enqueue(q.dequeue())

    def push(self,x):
        self.__q.enqueue(x)
        

    def pop(self):
        while not self.__q.isEmpty():
            self.__a=self.__q.dequeue()
            if not self.__q.isEmpty():
                self.__tq.enqueue(self.__a)

        self.__move_elements(self.__tq,self.__q)
        return self.__a                   
        
        
            

if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())