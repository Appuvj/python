

mixed_type={'vijay',23,123,True}
more_add ={'prasanth',22}

# add() method -> add element to the set

mixed_type.add('gym')
print('added in the list : ',mixed_type)

#update() method -> used to add 2 set 

mixed_type.update(more_add)
print('after updated : ',mixed_type)

# discard() method -> it will remove particular element 

mixed_type.discard('gym')
print('after discarding : ',mixed_type)

mixed_type.remove(123)
print('after removing : ',mixed_type)

