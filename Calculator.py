def  IsInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

txt = input('Please enter a math expression: ')
fields = txt.split()
if len(fields) != 3:
    print("Error: invalid Expression. Expected single line containing two"
          + "integers and operator similar to '3 + 5' ")
    exit(1)

if fields[1] not in set(['+', ])