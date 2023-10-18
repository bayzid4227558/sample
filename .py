

score = input("Please insert your Marks: ")
score = int(score)
print("abc")

if score >= 90:
    grade = "A+"
    print("your grade,'{}' is: {}"(score,grade))
elif score >= 80:
    grade = "B"
    print("your grade,'{}' is: {}"(grade))
elif score >= 70: 
    grade = "C"
    print("your grade,'{}' is: {}"(grade))
elif score >= 60:
    grade = "F"
    print("your grade,'{}' is: {}"(grade))
else:
    print("your grade fail " )

Vara = 10
print (not(Vara == 15))

bayzid = "sdsd"
print(not (bayzid == 'sds'))

num = 100
print(num > 10 or num < 20)

saarc = ["Bangladesh", "Afghanistan","Bhutan","Nepal","India","Pakistan", "Sri-lanka"]

country = input("-")

if country in saarc:
    print (country, " in member saarc")
else:
    print("member 001 ")

print("member 002 ")

print(25 != 25)

marks = int(input("Your result: "))

if marks % 2 == 0:
    print("Result of your provided symbol '{}' is: {}".format(marks,))
elif marks >= 70:
    grade = ("A")
    print("Result of your provided symbol '{}' is: {}".format(marks,grade))
elif marks >= 60:
    grade = ("A-")
    print("Result of your provided symbol '{}' is: {}".format(marks,grade))
elif marks >= 50:
    grade = ("B")
    print("Result of your provided symbol '{}' is: {}".format(marks,grade))
else:
    print("Fail")

import turtle 
turtle.forward(100)
turtle.exitonclick()

result = 0
for i in range(1,51,7):
    result += i
print(result)


numbers = [0,2,5,4,3,6,7,1,9]
max_n = numbers [0]
for i in numbers:
    if i > max_n:
        max_n = i 
print(max_n)

bayzid = [10,20,30,40,50,60000,700,80,90,100,200,300,400,]
bsh = bayzid[0]
for i in bayzid:
    if i > bsh:
        bsh = i 
print(bsh)

bf = [10,35,76,89,34,56,0,90,45,77,87]
gf = bf[5]
for x in bf:
    if x > gf:
        gf = x 
print (gf)

rs = 0
for z in  range (5,101,5) :
        print (z)
        rs += z
print (rs)

print("-----------------")

vs = 0
for x in range (50):
    if x % 5 == 0: 
        print(x)
        vs += x 
print (vs)


