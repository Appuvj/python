

Watch_details={
    'titan':8000,
    'fastrack':5000,
    'casio':10000,
    'titan':18000
}

#keys() -> returns a list containing the dictionary's key

key_method=Watch_details.keys()
print('key methods are : ',key_method)

value_method=Watch_details.values()
print('value method is : ',value_method)


# get method -> returns the value of specified key
get_method=Watch_details.get('casio')
print('get method of value casio : ',get_method)

# items() methods
item_method=Watch_details.items()
print('item method is : ',item_method)

#update method -> insert an item to the dist
Watch_details.update({'rolex':100000})
print('updated dist: ',Watch_details)

#pop method -> removes the element with the specified key
Watch_details.pop('titan')
print('removes the value from dist: ',Watch_details)
