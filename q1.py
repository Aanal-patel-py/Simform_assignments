X = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def gcd(a,b):
    while b:
        a, b = b, a % b
    print("value of a:",a)
    return a

def convert_to_words(num):
    num = str(num)
    words = ""
    i = 0
    while i < len(num):
        digit = int(num[i])
        match digit:
            case 0: words += "zero"
            case 1: words += "one"
            case 2: words += "two"
            case 3: words += "three"
            case 4: words += "four"
            case 5: words += "five"
            case 6: words += "six"
            case 7: words += "seven"
            case 8: words += "eight"
            case 9: words += "nine"
        i += 1
    return words





def convert_to_number(num):
    x=0
    again_number=""
    z=""
    while x<len(num):
        z+=num[x]
        print("value of z"+z)
        print(X.keys())
        if z in X.keys():
            print(True)
            print(X[z])
            again_number+=str(X[z])
            z=""
            
        x+=1
        print("The numbers is:",again_number)
    return again_number


numbers=input("Enter the numbers in words: ").split()
number1=int(convert_to_number(numbers[0]))
number2=int(convert_to_number(numbers[1]))
print("The numbers are:",number1,number2)
gcd_value=gcd(number1,number2)
output=convert_to_words(gcd_value)
print("The GCD of the numbers is:",output)
