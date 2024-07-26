
import arithmatic
print('select any operator')
print('1.Addition \n 2.Subtraction \n 3.Multiplication')
select=int(input('select 1/2/3 '))

def main():

    num01=int(input('enter first number: '))
    num02=int(input('enter second number: '))

    if(select == 1):
        Ans = arithmatic.addition(num01,num02)
        print(f'Addition {num01} and {num02}:',Ans)
    elif(select == 2):
        Ans = arithmatic.subtraction(num01,num02)
        print(f'Subtration {num01} and {num02}:',Ans)
    elif(select == 3):
        Ans = arithmatic.multiplication(num01,num02)
        print(f'Mutiplication {num01} and {num02}:',Ans)
    else:
        print('choose 1/2/3')

    



if __name__ == "__main__":
    main()


# import arithmatic

# def main():
#     print('Select any operator')
#     print('1. Addition\n2. Subtraction\n3. Multiplication')
#     select = int(input('Select 1/2/3: '))

#     num01 = int(input('Enter first number: '))
#     num02 = int(input('Enter second number: '))

#     operations = {
#         1: ('Addition', arithmatic.addition),
#         2: ('Subtraction', arithmatic.subtraction),
#         3: ('Multiplication', arithmatic.multiplication)
#     }

#     if select in operations:
#         operation_name, operation_func = operations[select]
#         Ans = operation_func(num01, num02)
#         print(f'{operation_name} of {num01} and {num02}: {Ans}')
#     else:
#         print('Invalid choice. Please select 1, 2, or 3.')

# if __name__ == "__main__":
#     main()
