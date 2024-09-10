class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, a):
        if len(self.stack) == self.size:
            print("Stack overflow")
        else:
            self.stack.append(a)

    def pop(self):
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def priority(self, a):
        if a == '+' or a == '-':
            return 1
        if a == '*' or a == '/':
            return 2
        if a == '^':
            return 3
        if a == '(':
            return 0
        return 0

    def infix_to_postfix(self, expression):
        postfix = []
        for char in expression:
            if char.isalnum():  
                postfix.append(char)
            elif char == '(':  
                self.push(char)
            elif char == ')':  
                x = self.pop()
                while x != '(':
                    postfix.append(x)
                    x = self.pop()
            else:  
                while self.stack and self.priority(self.stack[-1]) >= self.priority(char):
                    postfix.append(self.pop())
                self.push(char)



        while self.stack:
            postfix.append(self.pop())

        return ''.join(postfix)
obj = Stack(20)
expression = input("Enter the Expression: ")
result = obj.infix_to_postfix(expression)
print(f"The postfix expression is: {result}")
