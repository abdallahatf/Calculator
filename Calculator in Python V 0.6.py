import math

while True:
    num1 = float(input("1st num: "))
    operator = input("enter the operator: ")
    num2 = float(input("2nd num: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "\\":
        print("The operation is wrong\nRemember: divide is\"/\"")
    elif operator == "^":
        print(pow(num1, num2))
    elif operator == "c" or operator == "C":
        print(math.comb(int(num1), int(num2)))
    elif operator == "p" or operator == "P":
        print(math.perm(int(num1), int(num2)))
    else:
        print("the operation is wrong")
