from linkedStack import LinkedStack

class TwostackQueue:
    def __init__(self):
        self.__s = LinkedStack()
        self.__ts = LinkedStack()

    def __move(self,s,ts):
        while not s.isEmpty():
            ts.push(s.pop())

    def enqueue(self, x):
        self.__move(self.__s, self.__ts)
        self.__s.push(x)
        self.__move(self.__ts, self.__s)

    def dequeue(self):
        return self.__s.pop()



if __name__ == "__main__":
    at = TwostackQueue()
    at.enqueue(2)
    at.enqueue(3)
    at.enqueue(4)

    print(at.dequeue())
    print(at.dequeue())
    print(at.dequeue())