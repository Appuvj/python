#open() function -> fileName, mode(r,w,a,...)

# file_read = open('calculator.py','r')
# print(file_read.read())

import os
def createfile(filename):

    if(os.path.exists(filename)):
        print('file is already exist')
    else:
        file_create = open(filename,'w')

    

def main():
    print('enter the file name you want to create : ')
    file_name=input()

    createfile(file_name)


if __name__ == "__main__":
    main()
