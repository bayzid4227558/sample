
#Assigment of class:-o6

symbol_1st_input = input("press the symbol of your choice: +,-,*,/ :")

Number_2nd_input = input("press the number of your choice:1,2,--100 :")

Number_2nd_input = Number_2nd_input.split(" ")

print(Number_2nd_input)

result = 0 

for I in Number_2nd_input:
    if symbol_1st_input =="+":
        result = result + int(I)
print ("final result is:"+str(result))


if symbol_1st_input =="+":
    bayzid = I + Number_2nd_input
    print ("final result is: {}".format(bayzid))
elif symbol_1st_input =="-":
    bayzid = I - Number_2nd_input
    print ("final result is: {}".format(bayzid))
elif symbol_1st_input =="*":
    bayzid = I * Number_2nd_input
    print ("final result is: {}".format(bayzid))
elif symbol_1st_input =="/":
    bayzid = I / Number_2nd_input
    print ("final result is: {}".format(bayzid))
else :
    print ("code error") 

result = 0 

symbol_1st_input = input("press the symbol of your choice: +,-,*,/ : ")

vealu = 1

while vealu != 0:
    vealu = int(input("press the number of your choice:1,2,--100 : "))

    if symbol_1st_input =="+":
        result = result + vealu

print ("final result is: "+str(result))


for I in range(1,5):
    #print(I)
    for j in range(6,10):
        print(I,j)

veriable_list = [0,1,2,3,4,5,'bayzid','rhd','ptk']

#print(veriable_list)

for I in veriable_list:
    print("{}".format(I),end=" * ")

print(veriable_list[0:5])

#     if I ==5:
#         print("fuck")
#     else: 
#         print("{}\n".format(I))
        

    



