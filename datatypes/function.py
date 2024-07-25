# function:
# -> a function is a block of code that performs a specific task
# -> functions are reusable pieces of programs
# -> they allows you to give a name to a block of statement,allowing you to run that block using specified name anywhere
# in your program and any number of times
# -> the names given in the function definition are called paramaters
# whereas the values you supply in the function call are arguments
# -> you define a function with def keyword, then write identifier(name) followed by parantheses and a colon

# -> return -> used to exit from a function and go back to the function caller and return the specified value or 
               



def addition():
    print('inside addition')

addition()


def aaddition(value_01):
    print('inside addition')
    print('argument1 ',value_01)

aaddition(22)


def addition(value_01,value_02):
    print('inside addition')
    print('argument1 ',value_01)
    print('argument1 ',value_02)
    add=value_01+value_02
    return add
print(addition(22,18))

def calculation(value_01,value_02):
    print('inside addition')
    print('argument1 ',value_01)
    print('argument1 ',value_02)
    add=value_01+value_02
    sub=value_01-value_02
    return add,sub
print(calculation(22,18))



def calculation(value_01,value_02):
    print('inside addition')
    print('argument1 ',value_01)
    print('argument1 ',value_02)
    add=value_01+value_02
    sub=value_01-value_02
    return add,sub
res1,res2=calculation(10,20)
print('addition result : ',res1)
print('subtraction result : ',res2)

