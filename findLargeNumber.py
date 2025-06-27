#Write a program that takes 3 numbers as input and prints the largest one.

num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
num3=int(input("Enter number 3 :"))
num=[num1,num2,num3]

large=num[0]
for items in range(2):
    if num[items]>large:
        large=num[items]

print("Largest number is ",str(large))