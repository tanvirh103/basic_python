import getpass
import string

def checkPasswordStrength():
    password=getpass.getpass("Please Enter your Password: ")
    #print(password)
    if len(password)==0:
        print("Password length can't be 0")
        return False
    strength=0
    remarks=" "
    lowerCount=upperCount=numberCount=whiteSpaceCount=specialCount=0
    for char in list(password):
        if char in string.ascii_lowercase:
            lowerCount=lowerCount+1
        elif char in string.ascii_uppercase:
            upperCount=upperCount+1
        elif char in string.digits:
            numberCount=numberCount+1
        elif char==" ":
            whiteSpaceCount=whiteSpaceCount+1
        else:
            specialCount=specialCount+1

    if lowerCount >=1:
        strength=strength+1
    if upperCount >=1:
        strength=strength+1
    if numberCount >=1:
        strength=strength+1
    if specialCount >=2:
        strength=strength+2
    if whiteSpaceCount >=1:
        strength=strength+1

    if strength==1:
        remarks=("Very bad password.Change it as soon as possible")
    elif strength==2:
        remarks=("That's a weak password.You should change it")
    elif strength==3:
        remarks=("Your password is okay, but it can be improved.")
    elif strength==4:
        remarks=("Your password is hard to guess.But you could make it even more secure.")
    elif strength==5:
        remarks=("WOW that's a strong password!!!!You can continue with this password!")
    elif strength>=6:
        print("Wow that's a strong password!!!!!Hackers don't have a chance guessing that password!!")

    print("Your password has:-")
    print(lowerCount," lowercase letters")
    print(upperCount," uppercase letters")
    print(numberCount," digits")
    print(whiteSpaceCount,"whitespaces")
    print(specialCount,"special characters")
    print("Password Score: ",strength)
    print("Remarks: ",remarks)

def checkPassword(anotherPassword=False):
    valid=False
    if anotherPassword:
        choice=input("Do you want to check another password strength(Y/N):")
    else:
        choice=input("Do you want to check your password strength(Y/N): ")
    
    while not valid:
        if choice.upper()=="Y":
            return True
        elif choice.upper()=="N":
            print('Exiting.............')
            return False
        else:
            print("Invalid input...please try again.")
            return False
def main():
    print("======= Welcome to Password Strength Checker =======")
    checkp=checkPassword()
    #print(checkp)
    while checkp:
        checkPasswordStrength()
        checkp=checkPassword(True)

main()