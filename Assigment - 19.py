
# Through this program we can add, subtract, multiply and divide arithmetic numbers.

class Calculator:
    def addition(self, value1, value2):
        return value1 + value2

    def subtraction(self, value1, value2):
        return value1 - value2

    def multiplication(self, value1, value2):
        return value1 * value2

    def division(self, value1, value2):
        return value1 / value2

    def check_symbol(self, symbol, val1, val2):
        if symbol == "+":
            return self.addition(val1, val2)
        elif symbol == "-":
            return self.subtraction(val1, val2)
        elif symbol == "*":
            return self.multiplication(val1, val2)
        elif symbol == "/":
            return self.division(val1, val2)
        else:
            return "Invalid symbol input"

def run_calculator():
    calculator = Calculator()
    
    while True:
        symbol = input("Enter operation (+, -, *, /) or 'e' to End: ")
        if symbol == 'e':
            print("Code end")
            break
        
        val1 = int(input("Enter the first number: "))
        val2 = int(input("Enter the second number: "))
        
        result = calculator.check_symbol(symbol, val1, val2)
        print(f"Result: {result}")
        
        run_again = input("Do you want to execute it again? (y/n): ")
        if run_again != 'y':
            print("Code end")
            break

if __name__ == "__main__":
    run_calculator()