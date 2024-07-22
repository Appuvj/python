# range() : number of sequence
# start : default 0
# stop : excluded
# strp : default 1


for i in range(5):
  print(i)
print()


for i in range(5,10,2):
  print(i)
print()


for i in range(2,11):
  print(i)
print()


for i in range(2,int(11/2),2):  #11/2= 5.5
  print(i)
print()

for i in range(2,int(21/2),2):  
  print(i)
print()


author_name=('shakespear','apj abdulkalam','vijay kumar','prasanth','mani')

for auth in range(len(author_name)):   #range(5)
  print(auth)

  print()

for auth in range(len(author_name)):   #range(5)
    print(author_name[auth],'---',auth)


# iterate over a string using loop(range)
time_update ="its 4.15pm"

for time in range(len(time_update)):
      print(time_update[time])
