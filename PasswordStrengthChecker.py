#Question:
#Ask the user to input a password. Then check and print:\

#If it's less than 6 characters, say "Too weak".

#If it has at least one number and one letter and is at least 8 characters, say "Strong".

#Else, say "Moderate".
def password_checker(password):
    ln=len(password)
    has_letter=any(char.isalpha() for char in password)
    has_number=any(char.isdigit() for char in password)
    if ln<6:
        return "To weak"
    elif ln>=8 and has_letter and has_number:
        return "Strong"
    else:
        return "Moderate"

def main():
    password=str(input("enter your password :"))
    strength=password_checker(password)
    print(f"Password strength : {strength}")
if __name__ == "__main__":
    main()