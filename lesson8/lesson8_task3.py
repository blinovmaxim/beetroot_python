def make_operation(operation, *args):
    if not args:
        print("Empty Arguments!")
        exit(1)
    for arg in args:
        if type(arg) != int:
          raise ValueError("Operand not int")   
    operands = list(args)
    x = operands.pop(0)
    while operands:
        if operation == "+":
            x += operands.pop(0)
        elif operation == "-":
            x -= operands.pop(0)
        elif operation == "*":
            x *= operands.pop(0)
    return x
print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
