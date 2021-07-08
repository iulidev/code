# Calculator
# operand1 operator operand2
operand1 = input('Operand1: ')
operator = input('Operator: ')
operand2 = input('Operand2: ')
# print(type(operand1))
operand1 = float(operand1)
operand2 = float(operand2)

if operator == '+':
    print(operand1 + operand2)
elif operator == '-':
    print(operand1 - operand2)
elif operator == '/':
    if operand2 == 0:
        print('Impartire la zero!')
    else:
        print(operand1 / operand2)
elif operator == '*':
    print(operand1 * operand2)
else:
    print('Operator necunoscut')
