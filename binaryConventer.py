###############################################################################
#                                                                             #
#                                03.10.2022                                   #
#                   Ninas little play around with binary.                     #
#   - The program converts binary<->decimal and decimal<->hexadecimal         #
#                                                                             #
###############################################################################

# asks what the user wants to do
def select():
    print("Binary -> decimal = \"b2d\",\ndecimal -> binary = \"d2b\",\nhexa -> decimal = \"h2d\",\ndecimal -> hexa = \"d2h\"")
    choise = input("Command: ")
    if choise.upper() == "B2D":
        binary2decimal()
    elif choise.upper() == "D2B":
        decimal2binary()
    elif choise.upper() == "H2D":
        hexa2decimal()
    elif choise.upper() == "D2H":
        decimal2hexa()
    else:
        print("I can only handle so little. \"" + choise + "\" is too much!")

def hexa2decimal():
    hnumber = input("Hexadecimal: ")

    # creates a number adding correct values together by the correct algorythm
    def counting(number):
        # turns the hexa other way around to make index usage easier
        onumber = number[::-1]
        onumber = onumber.lower()
        lettersD = {"a":10, "b":11, "c":12,"d":13,"e":14,"f":15}
        added = 0
        indx = 0

        for i in onumber:
            if i in lettersD:
                added += lettersD[i]*16**indx
                indx += 1
            else:
                added += int(i)*16**indx
                indx += 1

        return added

    def check(input):
        input = input.lower()
        wrong = ""
        letters = "abcdef"
        numberlist = []
        for i in range(0,10):
            numberlist.append(i)
        
        for i in input:
            if i not in letters:
                try: 
                    number = int(i)
                    if number not in numberlist:
                        wrong = "y"
                except(ValueError):
                    wrong = "y"
                    
        if wrong == "y":
            print(f"I only handle \"{letters}\" and numbers from {min(numberlist)} to {max(numberlist)}.")
        else:
            print("-> " + str(counting(input)))

    check(hnumber)    

def decimal2hexa():
    number = int(input("Decimal: "))

    def counting(number):
        hexa = ""
        while number > 0:
            lettersD = {10:"a", 11:"b", 12:"c",13:"d",14:"e",15:"f"}
            aid = number % 16
            if aid in lettersD:
                hexa += lettersD[aid].upper()
            else:
                hexa += str(aid)
            number = (number-aid)/16
        return hexa[::-1]

    def check(number):
        try:
            number = int(number)
            print("-> " + counting(number))
        except(ValueError):
            print("I can only handle numbers. You entered: " + number)
    check(number)



def binary2decimal():
    bnumber = input("Binary: ")

    # Turns input string, counts all 1 with 2^(index of the 1) and adds them
    # up in one number (binary -> decimal) and returns it 
    def counting(number):  
        onumber = number[::-1]
        added = 0
        indx = 0
        for i in onumber:
            if i == "1":
                added += 2**indx
                indx += 1
            else:
                indx += 1
        return added

    # Checks if the input value is valid 
    def check(input):
        wrong = ""
        
        for i in input:
            # if something else than 0 and 1: takes it down
            if i != "0":
                if i != "1": 
                    wrong = "y"
                    break    
        # if something was wrong above: checks if too big length too and gives 
        # advice to the user
        if wrong == "y":
            print("Oi, there was something wrong with: " + input + ".")
        else:
            print("-> " + str(counting(bnumber)))

    check(bnumber)

# converts decimal to binary
def decimal2binary():
    dnumber = input("Decimal: ")

    def counting(number):
        binary = ""
        # Goes through the input decimal adding proper binary in order and
        #  returns it the correct way
        while number > 0:
            aid = number % 2
            if aid == 1:
                number = (number/2)-0.5
                binary += "1"
            else:
                number = number/2
                binary += "0"

        return binary[::-1]
    # Checks if the number is actually a number
    def check(number):
        try:
            number = int(number)
            print("-> " + counting(int(number)))
        except(ValueError):
            print("I only understand numbers. You inserted: " + number)
            
    check(dnumber)    


if __name__ == "__main__":
    select()
