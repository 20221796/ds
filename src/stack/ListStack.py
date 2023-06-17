class ListStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.insert(0,x) #리스트의 맨 앞을 탑으로 변경
        # self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop(0) #pop도 top을 리턴하도록 변경
        # return self.__stack.pop()
            
    def top(self):
        if self.isEmpty():
            print("No element in stack")
            return None
        else:
            return self.__stack[0]
        
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()

    def printStack(self):
        print("Stack:")

        for i in range(len(self.__stack), -1):
            print('stack[', i, ']:', self.__stack[i])