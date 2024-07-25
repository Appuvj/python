# dynamic input


def count_num(lst,number):
     count=0

     for i in lst:
          if(i==number):
               count +=1
     return count

def main():
    print('enter thr size of the list: ')
    size=int(input())
    data_input=[]
    print('enter thr values: ')
    for i in range(size):
        value = int(input())
        data_input.append(value)

    print('user list : ',data_input)

    searchnum= int(input('Enter element to be checked list:'))
    print(searchnum,"is repeating ",count_num(data_input,searchnum),"times")
 

if __name__ == "__main__":
        main()