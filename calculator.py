class Calculator:
    # initialise 2 attributes, inputs
    def __init__(self):
        self.input1 = float(input("Enter value for input 1: "))
        self.input2 = float(input("Enter value for input 2: "))

    def adder(self):
        return  self.input1 + self.input2

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2

    def divider(self):
        return (self.input1/self.input2)

    def clear(self):
        self.input1 =0
        self.input2 =0
        print("Cleared input 1 and 2 to 0")


Results = Calculator()
print("Result of input 1 + input 2:  ", Results.adder())
print("Result of input 1 - input 2:  ", Results.subtractor())
print("Result of input 1 * input 2:  ", Results.multiplier())
print("Result of input 1 / input 2:  ", Results.divider())
Results.clear()
