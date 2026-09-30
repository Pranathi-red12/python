#Data structures
#lists

'''a=[1,2,3,4,5,6,7,8,9,10]
print(a[1:2])
print(a[0:5])
print(a[2:8])
print(a[-1:-5:-1])
print(a[-1:-5])
print(a[::-1])
print(a[::])
print(a[8:-2])
print(a[-3:-2:1])
print(a[7:10])

a=[1,2,3,4,5,6,7,8,9,10]
b=[12,13,14]
a.append(11)
print(a)
a.insert(2,22)
print(a)
a.pop(5)
print(a)
a.pop()
print(a.count(2))
print(a.index(3))
a.remove(6)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#Harshad number
n=242
sum=0
temp=n
while n>0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
print(sum)
if temp%sum==0:
    print("Yes")
else:
    print("No")'''


#Nested list
'''students=[["Rahul",20,85],["Priya",19,90],["Arun",21,78]]
print(students)

a=[
  ["ravi",25,85],
  ["raju",26,89]
]
print(a[1][0])
a.append(["kumar",24,88])
b=[2,3,4]
c=[5,6,7]
print(b+c)
print(b*2)
print(2 in b)

a=(1,2,3,4)
print(a)
print(type(a))

a=1,2,3,4
print(a)
print(type(a))'''

#Tuple
'''t=(10,5,20)
print(t[::-1])

t=(10,5,20)
print(sorted(t))

t=(10,5,20)
print(sorted(t,reverse=True))'''

#Set
'''a={1,2,3,4,5,6,1,1,2,3,12}
print(a)

a={1,2,3,4,5,6,1,1,2,3,12}
a.add(17)
print(a)
a.update([16,22])
print(a)
a.update([89,98])
print(a)
a.discard(77)
print(a)
a.remove(12)
print(a)
a.pop()
print(a)
a.clear()
print(a)'''

#Task
#Fibonacci Numbers
'''a=0
b=1
n=10
print(a)
print(b)
for i in range(2,10):
    c=a+b
    print(c)
    a=b
    b=c'''

'''a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(a|b)
print(a.intersection(b))
print(a&b)
print(a.difference(b))
print(a-b)
print(a.symmetric_difference(b))
print(a^b)
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))'''

#Swap 2 variables
'''a=10
b=20
c=a
a=b
b=c
print(a)
print(b)

a=10
b=20
a,b=b,a
print(a)
print(b)

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)

a=10
b=20
a=a*b
b=a//b
a=a//b
print(a)
print(b)'''

#Task
'''n1=9
n2=12
ans=1
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        ans=i
print(ans)

n1=20
n2=40
ans=1
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        ans=i
print(ans)

a={1,2,3,4,5}
b=frozenset(a)
print(b)
print(a)
c=frozenset({4,5,6,7,8})
print(b.union(c))
print(b.intersection(c))
print(b.issubset(c))'''


#Dictionary
'''student={
    "name": "Raju",
    "age": 20,
    "course": "CSE",
    "marks": [20],
    "isPassed": True,
    2: "Raju",
    True: 4,
    3.14: "pi",
    "percentage": 65.6 }
d=dict(student)
print(d)


student={
    "name": "Raju",
    "age": 20,
    "course": "CSE",
    "marks": [20],
    "isPassed": True
}
print(student.get("name"))
student.update({
    "percentage":65,
    "grade":"D"
})
print(student.pop("isPassed"))
print(student)
print(student.popitem())
print(student)
print(student.keys())
print(student.values())
print(student.items())
dulicatestudent=student.copy()
print(dulicatestudent)'''

#Task
#Deficient numbers
n=10
sum=0
temp=n
for i in range(1,10):
    if n%i==0:
        sum=sum+i
print(sum)
if temp>sum:
    print("Is a deficient number")
else:
    print("Not a deficient number")
        

n=12
sum=0
temp=n
for i in range(1,12):
    if n%i==0:
        sum=sum+i
print(sum)
if temp>sum:
    print("Is a deficient number")
else:
    print("Not a deficient number")
    
    


















