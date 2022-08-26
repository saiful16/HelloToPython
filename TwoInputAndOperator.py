userInput1 = input("Plese enter the number")
num1= int(userInput1)

userOperator= input("Please enter an Operator")
oper = userOperator

userInput2 = input("Please enter the number")
num2= int(userInput2)



if oper == "+" :
    print(num1 + num2)
elif oper == "-" :
    print(num1-num2)
elif oper == "*"  :
    print(num1*num2)
elif oper == "/" :
    print(num1/num2)
