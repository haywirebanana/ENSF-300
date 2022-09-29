def checkint(integer):
    valid = ['-','0','1','2','3','4','5','6','7','8','9']
    while (0==0):
        y=0
        for i in integer:
            if i in valid:
                y = 1
                if i == '-' and len(i) < 2:
                    y = 0
                    integer = input("Invalid input, Please enter an integer number: ")
                continue
            else:
                y=0
                integer = input("Invalid input, Please enter an integer number: ")
                break        
        if y == 1:
            break    
    return int(integer)


def main():

    first_num = input('Enter first integer: ')
    first_num = checkint(first_num)

    first_op = input('Enter first operator: ')
    first_op = checkop(first_op)

    second_num = input('Enter second integer: ')
    second_num = checkint(second_num)

    second_op = input('Enter second operator: ')
    second_op = checkop(second_op)

    third_num = input('Enter third integer: ')
    third_num = checkint(third_num)

    integer_list = [first_num, second_num, third_num]
    operator_list = [first_op, second_op]

    value = evaluate(operator_list, integer_list)
    final_equation = equation(integer_list, operator_list, value)
    
    print(final_equation)

if __name__ == "__main__":
    main()
