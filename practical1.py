num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("\nSelect an operation: ")
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Division")
choice=int(input("Enter your choice(1-4): "))
if choice==1:
    print("Result 1:",num1+num2)
elif choice==2:
    print("Result 2: ",num1-num2)
elif choice==3:
    print("Result 3: ",num1*num2)
elif choice==4:
    if num2!=0:
        print("Result: ",num1/num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid Choice! Please enter 1,2,3 and 4.")
