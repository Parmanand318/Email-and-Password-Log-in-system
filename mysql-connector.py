import re
special_characters='!@#$%^&*()_+}{":?><,./;[]\|=-'
e=input("Enter your gmail")
flag=0
for each in special_characters:
    if each==[0]:
        print("invalid")
        flag=1
d=re.findall("^\d",e)
if d!=[]:
    print("invalid")
    flag=1
a=re.findall('.+@\.[a-z]',e)
if a!=[]:
    print("invalid")
    flag=1
if '@.' in e:
    print("invalid")
    flag=1
if flag==0:
    l=re.findall('.+@.+\.[a-z]',e)
    if l!=[]:
        print("valid")
else:
    print("invalid")

def password_validator(password):
    isLengthOk   = True if len(password)>5 and len(password)<16 else False
    isDigit_present = any(char.isdigit() for char in password)
    isLower_present = any(char.islower() for char in password)
    isUpper_present = any(char.isupper() for char in password)
    isSpecial_present = any(char in special_characters for char in password)

    isValid = all([isLengthOk , isDigit_present, isUpper_present, isSpecial_present, isLower_present])
    if isValid:
        print("Valid passowrd")
    else:
        print("Invalid password , Please follow password policy")
input_password = input("Create password ")
password_validator(input_password)