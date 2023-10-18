
# print(dir(builtins))
# import math 
# print(math.pi)
# print(math.pow(2,3))
# print(math.pow(3,2))
# print(math.sqrt(25))
# print(math.floor(5.2))
# print(math.ceil(5.2))

# import datetime as dt
# today = dt.date.today()
# print(today)

# import webbrowser
# url = "http://subin.com"
# print(webbrowser.open(url))

# import webbrowser as wb
# urrl = "http//subeen.com"
# print(wb.open(urrl))

# def find_fib(n):
#     if n <= 2:
#         return 1
#     fib_x, fib_next = 1, 1
#     i = 3 
#     while i <= n:
#         i += 1
#         fib_x,fib_next = fib_next, fib_x + fib_next
#         return fib_next
#     for x in range(1,11):
#         print(find_fib(x))
# n = 10
# for i in range (n):
#     print(f"I Love Bangladesh")

# import turtle
# turtle.shape("turtle")
# turtle.speed(1)
# for i in range(40):
#     turtle.forward(100)
#     turtle.left(45)
# turtle.exitonclick


# class Calculator:
#     def addition(self, value1, value2):
#         return value1 + value2

#     def subtraction(self, value1, value2):
#         return value1 - value2

#     def multiplication(self, value1, value2):
#         return value1 * value2

#     def division(self, value1, value2):
#         return value1 / value2

#     def check_symbol(self, symbol, val1, val2):
#         if symbol == "+":
#             return self.addition(val1, val2)
#         elif symbol == "-":
#             return self.subtraction(val1, val2)
#         elif symbol == "*":
#             return self.multiplication(val1, val2)
#         elif symbol == "/":
#             return self.division(val1, val2)
#         else:
#             return "Invalid symbol input"

# def run_calculator():
#     calculator = Calculator()
    
#     while True:
#         symbol = input("Enter operation (+, -, *, /) or 'e' to End: ")
#         if symbol == 'e':
#             print("Code end")
#             break
        
#         val1 = int(input("Enter the first number: "))
#         val2 = int(input("Enter the second number: "))
        
#         result = calculator.check_symbol(symbol, val1, val2)
#         print(f"Result: {result}")
        
#         run_again = input("Do you want to execute it again? (y/n): ")
#         if run_again != 'y':
#             print("Code end")
#             break

# if __name__ == "__main__":
#     run_calculator()
 
# import turtle
# turtle.shape("turtle")
# turtle.speed(1)

# for side_length in range(50,100,10):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)
# turtle.exitonclick

saarc = ["Bangladesh","Afghanistan","Bhutan","Nepal","India","Pakistan","Sri Lanka"]

for country in saarc:
    print(country,"is a member of saarc")












