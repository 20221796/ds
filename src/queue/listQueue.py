class ListQueue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,x):
        self.queue.append(x)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[0]
    
    def isEmpty(self) -> bool:
        return (len(self.queue) == 0)
    
    def dequeueAll(self):
        self.queue.clear()
    
    def printQueue(self):
        print("Queue from front:", end=' ')
        for i in range(len(self.queue)):
            print(self.queue[i], end=' ')
        print()