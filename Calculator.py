print("----Calculator----")
num1=int(input())
num2=int(input())

symbols= input("Enter any symbol(+,-,/,*)")

def add():
    sum= (num1+num2)
    print(sum)
def subtract():
    difference= (num1-num2)
    print(difference)
def multiply():
    multiplication= (num1*num2)
    print(multiplication)
def divide():
    division= (num1/num2)
    print(division)

if symbols=="+":
    add()
elif symbols=="-":
    subtract()
elif symbols =="/":
    if num2==0:
        print("Cannot be divided by 0")
    else:
        divide()
elif symbols== "*":
    multiply()
else:
    print("Invalid operator")


    