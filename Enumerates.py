                   #[ Enumerate and Constants in Python ]
#[ enumerate... ]
x=['umar','javed','jutt']
for index,x in enumerate(x,start=1):
    print(index,x)

print("_______________")

x=['umar','javed','jutt']
for index,x in enumerate(x):
    print(x)
    if(index==2):
     print('is a Caste')

