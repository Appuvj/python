#  Write a program which will check the number is greater 
# and equal to 70 and less than and equal to 90

def greater(number):

    if(number>=70 and number<=90):
        return number

def main():
    size=int(input('enter the size : '))

    lst=[]
    print("enter the values: ")

    for i in range(size):
        value=int(input())
        lst.append(value)
    print('the list is : ',lst)

    filter_list=list(filter(greater,lst))
    print('the filter list is : ',filter_list)


if __name__ =="__main__":
    main()