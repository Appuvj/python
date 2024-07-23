#  f-string : 
#  to insert a varaible value into a string
#  place the letter f immediately before opening the quotation mark
#  put braces around the variable names
#  python will replace each variable with its value when string is displayed
#  these strings are called f-string
#  f-string was introduced in python 3.6
#  earlier 


student_name=input("enter your name ")
student__id= int(input("enter your id "))
# print(f"student name :{student_name.title()} \n student id :{student__id}")
# print(f"student name :{student_name.upper()} \n student id :{student__id}")


# format method
print("student name :{} \n student id :{}".format(student_name,student__id))
print("student name :{} \n student id :{}".format(student__id,student_name))     # order must not change


