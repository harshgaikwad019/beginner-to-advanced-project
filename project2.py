def get_number():
      while True:
            operand = input("number: ")
            try:
                return float(operand)
            except:
                print("invalid number, try again. ")

operand = get_number()
operand2 =get_number()
sign = input("sign: ")

print(operand, sign, operand2)

result = 0
if sign == "+":
    result = operand + operand2
elif sign == "-":
        result = operand - operand2
elif sign == "*":
        result = operand * operand2
elif sign == "/":
    if operand2 != 0:
            result = operand / operand2
    else:
        print('division by zero.')
print(result)