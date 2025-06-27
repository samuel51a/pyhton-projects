num1=input("Enter first number :")
num2=input("Enter second number :")
operation=input("Choose operation (+,-,*,/) :")
try:
    num1=float(num1)
    num2=float(num2)

    if operation=='+':
        print(int(num1)+int(num2))
    elif operation=='-':
        print(int(num1)-int(num2))
    elif operation=='*':
        print(int(num1)*int(num2))
    elif operation=='/':
        print(int(num1)/int(num2))
    else:
        print("Please enter valid operation")
except ValueError:
    print("Enter a valid number.")
