age=-1
while age<0:
    age=input("Enter your age: ")
    age=int(age)

if age<18:
    print("You are a minor.")
elif age>18 and age<65:
    print("You are an udult")
else:
    print("You are a senior citizen.")
