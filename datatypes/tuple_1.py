#create a tuple
#homogenus
student_id =(123,124,125,126)
ice_cream=('choculate','vanila','strawberry')

#heterogenus
mixed_type=(123,'hello',False,58.23)

#len()
#using index ==> strawberry(positive index)
#using slicing ==> 'Hello',False

print('the length is : ',len(student_id))
print('the data is : ',ice_cream[2])

print('the data is : ',mixed_type[-2])

print('the data is : ',mixed_type[1:3])



ice_creame = ('Vanilla')        # str
print(ice_creame,type(ice_creame))
ice_creame = ('Vanilla',)       # comma (tuple)
print(ice_creame,type(ice_creame))

# immutable
# mixed_type[0] = True
# print("False ",mixed_type)


ice_cream=('vanilla','choco','blueberry','vanilla')

countmethod = ice_cream.count('vanilla')
print('count method: ',countmethod)
print()

indexmethod = ice_cream.index('vanilla')
print('index method: ',indexmethod)