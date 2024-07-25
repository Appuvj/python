#  Write a program which will check the number is greater 
# and equal to 70 and less than and equal to 90


def main():

    size=int(input('enter thye size : '))

    lst=[]
    print('enter the values : ')

    for i in range(size):
        value=int(input())

        lst.append(value)
    print('the list is : ',lst)

    filter_list=list(filter(lambda number : number>=70 and number<=90,lst))
    print('the filter list lambda is : ',filter_list)


if __name__ =="__main__":
    main()

