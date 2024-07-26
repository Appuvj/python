

# def sum_all(*args):
#     count=0
#     for i in args:
#         count+=i
#     return count
    
# output=sum_all(1,2,3,4,5,6,7,8,9,10)
# print('addition : ',output)

#                      ** => keyword argument

def staffdetails(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} is {value}')
def main():
    changepond = {'Name':'vijay',
                  'Age':23,
                  'MobileNo':9768657767
                 }
    staffdetails(**changepond)
if __name__ =="__main__":
    main()




# def change(changepond):

#     for i in changepond:
#         caps=i.capitalize()
#         print('the list is : ',caps)
        

# def main():
#     changepond=['gokul','ajith','suresh','vijay']
    

#     change(changepond)

# if __name__ == "__main__":
#     main()


    
