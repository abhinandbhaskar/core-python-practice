import collections
class Stack:
    def __init__(self):
        self.stack=collections.deque()
    def Stack_Op(self):
        inp=int(input("Enter the number of elements : "))
        for i in range(0,inp):
            element=int(input(f"Enter the element{i+1} : "))
            self.stack.append(element)
        while True:
            choice=int(input("Choice 1.pop 2.quit"))
            if choice==1:
                e=self.stack.pop()
                print("Poped value",e)
                print("Stack",self.stack)
            elif choice==2:
                break

obj=Stack()
obj.Stack_Op()
