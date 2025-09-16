# Problem-1: Calculator (add,sub,multiply,divide)

class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Division by zero not possible"
            else:
                return self.a / self.b
        else:
            return "Invalid operation"


#  Main Program 
print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add / subtract / multiply / divide): ")

calc = Calculator(a, b, op)
print("Result =", calc.calculate())
