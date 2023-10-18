
# Through this program we can add, subtract, multiply and divide arithmetic numbers.

import Assigment14

if __name__ == "__main__":
    input_A = int(input("press the 1st number of your choice:1,2,--100 :"))
    input_B = int(input("press the 2nd number of your choice:1,2,--100 :"))
    Symbol = input("press the symbol of your choice: +,-,*,/ :")

    if Symbol == Assigment14.addition_chech():
        result = Assigment14.addition(input_A,input_B)
        print(f'{input_A} {Symbol} {input_B} = {result}')

    elif Symbol == Assigment14.minus_chech:
        result = Assigment14.minus(input_A,input_B)
        print(f'{input_A} {Symbol} {input_B} = {result}')
              
    elif Symbol == Assigment14.multiplication_chech:
        result = Assigment14.multiplication(input_A,input_B)
        print(f'{input_A} {Symbol} {input_B} = {result}')
              
    elif Symbol == Assigment14.division_chech:
        result = Assigment14.division(input_A,input_B)
        print(f'{input_A} {Symbol} {input_B} = {result}')
    else:
        print("invalid symbol input")

print("Code End")  

    

    
    





