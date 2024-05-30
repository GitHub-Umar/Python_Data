                           #[ File Handling in Python ]
#[ read/write/create/delete files and exception handling  ]
file=open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python.txt","r")
print(file.read())
file.close()

print("_______________")

#[ exception handling ]
try:
    file = open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\code.txt", "r")
    print(file.read())
except:
    print("File not avaliable")

print("_______________")

#[ wrirte new file copy of existing file ]
with open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python.txt","r") as f2:
    with open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python1.txt","w") as f3:
        for i in f2:
            f3.write(i)
file=open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python1.txt","r")
print(file.read())

print("_______________")

#[ append file ]
file=open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python1.txt", "a")
file.write("\npython is a best")
file=open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python1.txt","r")
print(file.read())

print("_______________")

 #[ create file ]
 # file=open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python.txt","x")

#[ write a file ]
# file=open("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python.txt","w")
# file.write("Python is a programming language")

#[ remove file ]
# import os
# os.remove("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python3.txt")


#[ remove using loop ]
import os
if os.path.exists("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python4.txt"):
  os.remove("C:\\Users\\HP EliteBook\\Desktop\\New folder\\python4.txt")
else:
  print("The file does not exist")

#[ Folder Delete ]
# import os
# os.rmdir("C:\\Users\\HP EliteBook\\Desktop\\myfolder")




















