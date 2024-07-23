company={'infosys','icici bank','tcs','bajaj'}
add_company={'sbi','tata consultancy','infosys','tcs'}


# union_method -> it will return all the elements
union_method=company.union(add_company)
print('union method is : ',union_method)
print()

union_method=company|add_company
print('using operator : ',union_method)
print()

intersection_method=company.intersection(add_company)  #operator &
print('intersection method will return the common element: ',intersection_method)
print()

difference_method=company.difference(add_company)  # it bring the elemets which is not common on the left set (company)
print('difference method ',difference_method)
print()

difference_method=add_company.difference(company)  # it bring the elemets which is not common on the left set (add_company)
print('difference method ',difference_method)
print()

symm_difference = company.symmetric_difference(add_company)
print('symm_difference: ',symm_difference)






