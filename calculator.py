def calculation(num1,num2,operation):
        try:
            num1=float(num1)
            num2=float(num2)

            if operation=='+':
                return num1+num2
            elif operation=='-':
                return num1-num2
            elif operation=='*':
                return num1*num2
            elif operation=='/':
                return num1/num2
            else:   
                return "Please enter valid operation"
        except ValueError:
            return "Enter a valid number."

def main():

    num1=input("Enter first number :")
    num2=input("Enter second number :")
    operation=input("Choose operation (+,-,*,/) :")
    results=calculation(num1,num2,operation)
    print(results)
if __name__ == "__main__":
    main()