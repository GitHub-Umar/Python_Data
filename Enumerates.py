                   #[ Enumerate and Constants in Python ]
#[ enumerate ]
x=['umar','javed','jutt']
for index,x in enumerate(x,start=1):
    print(index,x)

print("_______________")

x=['umar','javed','jutt']
for index,x in enumerate(x):
    print(x)
    if(index==2):
     print('is a Caste')

print("_______________")

fruits=['apple','banana','mango']
count =1
for x in fruits:
    print(count,x)
    count+=1

print("_______________")

students=['umar','ali','ahmad']
for count in range(len(students)):
    print(count+1,students[count])


