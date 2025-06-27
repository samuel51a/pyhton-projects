#Question:
#Ask the user to input a password. Then check and print:\

#If it's less than 6 characters, say "Too weak".

#If it has at least one number and one letter and is at least 8 characters, say "Strong".

#Else, say "Moderate".

password=str(input("enter your password :"))
ln=len(password)


if ln<6:
    print("Too weak")
elif ln>=8 and password.isalnum:
    print("Strong")
else:
    print("Moderate")
