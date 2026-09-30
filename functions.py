'''def greet():
    print("Hello!")
greet()
greet()
greet()
greet()

def greet():
    print("PRA")
greet()
greet()
greet()
greet()

def help():
    print("Execute program in laptop")
help()
help()

def printOneToTen():
    for i in range(0,11):
        print(i)
printOneToTen()
printOneToTen()
printOneToTen()

def sum():
    a=5
    b=3
    print(a+b)
sum()
sum()
sum()

def minus():
    a=5
    b=3
    print(a-b)
minus()
minus()
minus()

def multiply():
    a=5
    b=3
    print(a*b)
multiply()
multiply()
multiply()

def divide():
    a=5
    b=3
    print(a/b)
divide()
divide()
divide()

def floor():
    a=5
    b=3
    print(a//b)
floor()
floor()
floor()

def mod():
    a=5
    b=3
    print(a%b)
mod()
mod()
mod()

def expo():
    a=5
    b=3
    print(a**b)
expo()
expo()
expo()

def greet(name):
    print("Hello",name)
greet("Ravi")
greet("Sita")
greet("Kiran")

def sum(a,b):
    print(a+b)
sum(2,3)
sum(1,1)

def multiply(a,b,c):
    print(a*b*c)
multiply(2,3,4)
multiply(8,9,10)

def square(a):
    print("Area of square",a*a)
square(4)

def rectangle(a,b):
    print("Area of rectangle",a*b)
rectangle(4,2)

def sum(a,b):
    result=a+b
    return result
add=sum(1,2)
print(add)

def sum(a,b):
    result=a+b
    return result
x=sum(1,2)
print(x*5)
y=sum(3,4)
print(y)
z=sum(4,5)
print(z*8)

def max(a,b):
    if a>b:
        return a
    else:
        return b
x=max(10,20)
print(x)

def can_vote(age):
    if age>=18:
        return True
    else:
        return False
x=can_vote(20)
print(x)


def sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
x=sum_n(5)
print(x)

def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
x=reverse(1234)
print(x)

def palindrome(n):
    temp=n
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    if rev==temp:
        return True
    else:
        return False
print(palindrome(121))

def total(price,quantity):
    total_price=price*quantity
    return total_price
x=total(100,5)*0.9
print(x)

def total_marks(m1,m2,m3):
    return m1+m2+m3
x=total_marks(80,75,90)*100/300
print(x)'''

#Arguments
'''def mult(a,b,c,d):
    print(a*b*c*d)
mult(1,2,3,4)
mult(c=5,d=3,a=4,b=7)

def greet(name,message="I am Cult"):
    print(message,name)
greet("Hassine")
greet("Hassine and my age is 64 and my brother is Chintu Model Kothapet","I am Kodad model")

def divide(a,b):
    print(a/b)
divide(89,98)
divide(b=77,a=00)

def floor(a,b):
    print(a//b)
floor(89,98)
floor(b=77,a=00)

def mod(a,b):
    print(a%b)
mod(89,98)
mod(b=77,a=00)

def expo(a,b):
    print(a**b)
expo(89,98)
expo(b=77,a=00)

def sub(a,b):
    print(a-b)
sub(89,98)
sub(b=77,a=00)

def add(a,b):
    print(a+b)
add(89,98)
add(b=77,a=00)'''


#Variable-Length arguments
'''def help(*a):
    print(a)
help(1,2)

def help(b,*a):
    print(a,b)
    print(type(a))
help(1,2)
help(4,5,6,7)

def help(c,*a,b):
    print(b,a,c)
    print(type(a))
help(1,2,5,b=8)
help(4,5,6,7,b=12)

def help2(*c,b):
    print(b,c)
help2(7,8,9,b=22)

def student(*a,**details):
    print(a,details)
    print(type(details))
    print(details['name'])
student(name="Ravi",age=25,city="Hyderabad")

def student(*a,**details):
    print(details,a)
    print(type(details))
    print(details['name'])
student(1,2,name="Ravi",age=25,city="Hyderabad")'''

#Unpacking
'''num=[1,2,3,4,5,6]
a,*b=num
print(a,b)
*c,d=num
print(c,d)
x,*y,z=num
print(x,y,z)
m,n,*p=num
print(m,n,p)'''

#Multiple return values
'''def help(a,b):
    s=a+b
    p=a*b
    sub=a-b
    return s,p,sub
x,y,y2=help(2,3)
print(x,y,y2)
z=help(7,8)
print(z)'''


#forward approach
'''def gcd(n1,n2):
    ans=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            ans=i
    return ans
x=gcd(20,40)
print(x) 

def lcm(n1,n2):
    ans=1
    for i in range(min(n1,n2),-1):
        if n1%i==0 and n2%i==0:
            ans=i
    return ans
x=lcm(9,12)
print(x)'''

#backward approach
'''def gcd(n1,n2):
    ans=1
    for i in range(min(n1,n2),0,-1):
        if n1%i==0 and n2%i==0:
            ans=i
            break
    return ans
x=gcd(20,40)
print(x)'''

#Global variable + Local variable with same name
'''x=10
def test():
    x=20
    print(x)
test()
print(x)

a=10
def help():
    global a
    a=40
    print(a)
help()
print(a)'''

#lambda/anonymous functions
'''add2=lambda a,b:a+b
y=add2(7,8)
print(y)

square=lambda a:a*a
y=square(4)
print(y)

maxi=lambda a,b:max(a,b)
y=maxi(2,9)
print(y)

mini=lambda a,b,c:min(a,b,c)
y=mini(3,8,0)
print(y)

convert=lambda a:a.upper()
print(convert("abc"))

check=lambda a:a%2==0
print(check(3))

l1=["abc","ravi","raju","ramu"]
convert=list(map(lambda x:x.upper(),l1))
print(convert)

l2=[12,4,5,8,15]
add=list(map(lambda x:x+10,l2))
print(add)

numbers=[1,2,3,4,5]
cubes=list(map(lambda a:a**3,numbers))
print(cubes)

celsius=[0,10,20,30,40]
temp=list(map(lambda c:(c*9/5)+32,celsius))
print(temp)

#filter
l1=[3,6,7,9,12,34]
result2=list(filter(lambda a:a%2!=0,l1))
print(result2)

l2=[55,24,52,67,11,44]
result3=list(filter(lambda a:a>=50,l2))
print(result3)

l3=[-2,4,6,-4,2,22,-55]
result4=list(filter(lambda a:a>=0,l3))
print(result4)

l4=[15,2,20,25,30,22,44,11]
result5=list(filter(lambda a:a%5==0,l4))
print(result5)

names=["Ram","Alexander","John","Christopher","Bob"]
result6=list(filter(lambda a:len(a)>=5,names))
print(result6)'''

#Recursion
'''def help():
    print("hello")
    help()
help()

def help(n):
    if n==0:
        return
    print("hello")
    help(n-1)
help(5)

def help(i,n):
    if i>n:
        return
    print(i)
    help(i+1,n)
help(1,5)'''

#Task
'''def help(i,n):
    if i<n:
        return
    print(i)
    help(i-1,n)
help(5,1)'''
    

#Factorial of number
'''def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
ans=fact(5)
print(ans)'''

#Fibonacci
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(4))








 
















































