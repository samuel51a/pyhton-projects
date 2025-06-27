import sys

try:
    if len(sys.argv)==4:
        num1=float(sys.argv[1])
        num2=float(sys.argv[2])
        operator=sys.argv[3]
        if operator=="+":
            print(num1 + num2)
        elif operator=="*":
            print(num1 * num2)
        elif operator=="-":
            print(num1-num2)
        elif operator=="/":
            if num2==0:
                print("Please make sure num2 is not zero.")
            else:
                print(num1/num2)
        else:
            print("Please enter valid operator (+,-,*,/) :")
    else:
        print("Enter a valid values")
except ValueError:
    print("Please enter valid numbers")