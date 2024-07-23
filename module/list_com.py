# using for loop you have to create a list of square numbers 





def main():

    numbers=int(input('enter the size: '))
    result=[]

    for i in range(numbers+1):

        result.append(i**2)

    print(result)

if __name__ == "__main__":
    main()

