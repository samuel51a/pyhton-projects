import sys

if len(sys.argv)>2:
    num1=sys.argv[1]
    num2=sys.argv[2]
    sum=int(num1)+int(num2)
    print("Sum is :",sum)
else:
    print("No numbers provided")

