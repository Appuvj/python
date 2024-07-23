# set:
# -> collection of items
# -> enclosed in {}
# -> each element is seperated by ,
# -> unordered
# -> mutable
# -> unique

staff_id={123,124,125,126}  # same datatype

mixed_type={'vijay',23,123,True} # mixed data type

print('set', mixed_type)
print('length of set', len(mixed_type))

s1={True,0,1,False}
print(s1)
# true - 1
# false - 0

s1={True,1}
print(s1)


#task
mixed_type={'vijay',23,123,True}

for name in mixed_type:
    print(f'{name}, details')


