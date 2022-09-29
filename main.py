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
