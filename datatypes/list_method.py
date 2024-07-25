# menu_card=['panner','dal','rice']
# print('available items in menu card :',menu_card)

# #append()--> adds an element at the end of the list

# menu_card.append('channa')
# print('available items in menu card  after append :',menu_card)

# # briyani,pani puri
# #extend()--> add the element of a list(or iterable)
# #to the end of list

# menu_card.extend(['briyani','pani puri'])
# print('available items in after extend :',menu_card) 

# #insert --> adds an element at the specified position

# menu_card.insert(1,'prawn fry')
# print('available items in menu card after insert:',menu_card)

# #remove() method -> will remove specified position

# menu_card.remove('dal')
# print('available items in menu card after remove:',menu_card)

# #pop() method -> removes element of specified position based on index

# menu_card.pop(2)
# print('available items in menu card after pop :',menu_card)


menu_card=['panner','dal','rice']
#index method
index_method=menu_card.index('rice')
print('it will give position:',index_method)

index_method=menu_card.index('panner')
print('it will give position:',index_method)


#sort method
menu_card.sort()
print('it will sort :',menu_card)

