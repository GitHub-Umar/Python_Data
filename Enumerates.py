
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








print("_______________")



# def print_star_pattern(rows):
#     for i in range(1, rows + 1):
#         print("*" * i)
#
# rows = int(input("Enter the number of rows: "))
# print_star_pattern(rows)

print("_______________")

# def print_star_pattern(rows):
#     i = 1
#     while i <= rows:
#         print("*" * i)
#         i += 1
#
# rows = int(input("Enter the number of rows: "))
# print_star_pattern(rows)

#
# def print_star_pattern(rows):
#     for i in range(1, rows + 1):
#         print("*" * i)
#
# rows = 5  # You can change this number to adjust the number of rows in the pattern
# print_star_pattern(rows)










