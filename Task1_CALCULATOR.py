
print("*"*7+"  Welcome to Calculator  "+"*"*7)
while True:
    print()
    print("For addition------- ---Type 1")
    print("For subtraction------- Type 2")
    print("For multipliaction---- Type 3")
    print("For division---------- Type 4")
    print("For exiting------------Type 5")
    print()
    choice=int(input("Enter your choice: "))
    print()
    if choice == 5:
        print("Exiting the Calculator")
        break
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == 1:
        num3 = num1 + num2
        print("The addition of %d and %d is %d" %(num1, num2, num3))
    elif choice == 2:
        num3 = num1 - num2
        if num3 >= 0:
            print("The subtraction of %d and %d is %d"  %(num1, num2, num3))
        else:
            print("The subtraction of %d and %d is %d"  %(num1, num2, -num3))
    elif choice == 3:
        num3 = num1 * num2
        print("The multiplication of %d and %d is %d"  %(num1, num2, num3))
    elif choice == 4:
        num3 = num1 / num2
        print("The division of %d and %d is %d"  %(num1, num2, num3))
