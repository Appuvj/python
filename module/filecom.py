import os
import filecmp

def comparefiles(filename1,filename2):
    if(not os.path.exists(filename1)):
        print('not exist : ',filename1)
    elif(not os.path.exists(filename2)):
        print('not exist : ',filename2)
    else:                                               
        compare = filecmp.cmp(filename1,filename2)
        print('after comparing: ',compare)
    

def main():
    file_01=input('enter the first file : ')
    file_02=input('enter the second file name : ')

    comparefiles(file_01,file_02)


if __name__ == "__main__":
    main()

    

