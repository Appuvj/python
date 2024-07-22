# Dictionary
# -> a dictionary is a collection of key:value pair
# -> here, each key is connected to a value
# -> use a key to access the value 
# -> key must be unique

Watch_details={
    'titan':8000,
    'fastrack':5000,
    'casio':10000,
    'titan':3000
}

print('watch details',Watch_details)  # titan (consider the latest key value)
print(len(Watch_details))
print(type(Watch_details))
print('using key' ,Watch_details['titan'])

Watch_details={
    'titan':8000,
    'fastrack':5000,
    'casio':10000,
    'rolex':8000
}


print('watch details',Watch_details)  
print(len(Watch_details))
print(type(Watch_details))
print('using key' ,Watch_details['titan'])
print('using key' ,Watch_details['rolex'])


Watch_details['rolex']=100000
print('after modifing: ',Watch_details)

Watch_details['Indian Terrain']=1000000
print('adding new watch: ',Watch_details)


# create a dictionary of food items and price

Food_items={
    'briyani':200,
    'grill':400,
    'tandoori':450,
    'mandi':500
}

Food_items ['briyani']=250
print('after modifing : ',Food_items)

Food_items ['BBQ']=600
print('adding product : ',Food_items)



# Nested dictionary 

user={
    'vijaydetails':{
    'firstname':'vijay',
    'lastname':'kumar',
    'location':'chennai',
    
},

'prsanthdetails':{
    'firstname':'prasanth',
    'lastname':'mani',
    'location':'thiruthani',
},

'ajithdetails':{
    'firstname':'ajith',
    'lastname':'kumar',
    'location':'guduvanjery',
}

}

for details in user:
    print(details)
    print(user[details ])

print(user ['vijaydetails'] ['firstname'])
print()
print(user ['vijaydetails']['location'])
