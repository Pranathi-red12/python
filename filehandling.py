'''file=open("students.txt","r")
data=file.read()
print(data)
file.close()

file=open("students.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open("students.txt","r")
data=file.readlines()
print(data)
file.close()

file=open("students.txt","w")
file.write("Pranathi\nSrinithya\n")
file.write("Hassine")
file.close()
file=open("students.txt","r")
data=file.read()
print(data)
file.close()
print("writing is done man")

file=open("students.txt","a")
file.write("\nPranathi\n")
file.write("Hassine")
file.close()
print("appended done")'''

#Task
'''file=open("marks.txt","w")
file.write("50\n")
file.write("64\n")
file.write("72\n")
file.write("85\n")
file.write("96\n")
file.close()
file=open("marks.txt","r")
data=file.read()
print(data)
file.close()'''

'''file=open("students.txt","w")
students=["Priya\n","Vani\n","Rahul"]
file.writelines(students)
file.close()
print("Done man")

file=open("csmb3.txt","x")
file.write("hello bro")
file.close()
print("file is created")'''

#File properties
'''file=open("students.txt","r")
print(file.name)
print(file.mode)
print(file.closed)
file.close()
print(file.closed)'''

#File built-in methods
#tell()
'''file=open("students.txt","r")
data=file.read(15)
print(data)
x=file.tell()
print(x)
data2=file.read()
print(data2)
file.close()'''

#seek()
file=open("students.txt","r")
print(file.read(5))
file.seek(0)
print(file.read(5))
file.close()


















