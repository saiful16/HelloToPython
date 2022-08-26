userInput1 =input("Please enter the First Number : ")
number1= int(userInput1)

userInput2= input("Please enter the Second Number")
number2 = int(userInput2)

if number1 > number2 :
    print(number1," is bigger")
elif number2 > number1 :
    print(number2, "is bigger")
else:
    print("Somethings else")
