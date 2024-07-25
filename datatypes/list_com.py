#using list comprehension creating a list of square numbers

# new_list= [expression for member in iterable]

# new_list= [expression for member in iterable if(optional)]

new_list = [i for i in range(1,11)]
print('list comprehension: ',new_list)


new_list = [i for i in range(1,11) if(i%2==0)]
print('list comprehension: ',new_list)

vovels=['a','e','i','o','u']
name='vijay'
new_list= [i for i in name if(i in vovels)]
print('list comprehension in name is : ',new_list)