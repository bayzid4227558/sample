

# Through this program we can add, subtract, multiply and divide arithmetic numbers.

def add(a,b,Symbol):
    if Symbol == "+":
        result = (a+b)
        return result
    elif Symbol == "-":
        result = (a-b)
        return result
    elif Symbol == "*":
        result = (a*b)
        return result
    elif Symbol == "/":
        result = (a/b)
        return result
    else:
        print("funtion not defind")


input_A = float(input("press the 1st number of your choice:1,2,--100 :"))
input_B = float(input("press the 2nd number of your choice:1,2,--100 :"))
Symbol = input("press the symbol of your choice: +,-,*,/ :")

result = add(input_A,input_B,Symbol)
print(f'{input_A} {Symbol} {input_B} = {result}')



