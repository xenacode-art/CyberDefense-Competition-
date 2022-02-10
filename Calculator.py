def IsInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


txt = input('Please enter a math expression: ')
fields = txt.split()
if len(fields) != 3:
    print("Error: invalid Expression. Expected single line containing two "
          + "integers and operator similar to '3 + 5' ")
    exit(1)
if not IsInt(fields[0]) or not IsInt(fields[2]):
    print("Error: one of the numbers is incorrect")
    exit(1)

if fields[1] not in {'+', '-', '/', '*' and '%'}:
    print("Error: unexpected operator. Expected one of +,-,* and % ")
    exit(1)
operand1 = int(fields[0])
operand2 = int(fields[2])
if fields[1] == '+':
    result = operand1 + operand2
elif fields[1] == '-':
    result = operand1 - operand2
elif fields[1] == '*':
    result = operand1 * operand2
elif fields[1] == '%':
    result = operand1 % operand2
print(txt, "=", result)
