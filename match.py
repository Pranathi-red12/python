'''day="Monday"
match day:
    case "Monday":
        print(1)
    case "Tuesday":
        print(2)
    case "wednesday":
        print(3)
    case "Thursday":
        print(4)
    case "Friday":
        print(5)
    case "Saturday":
        print(6)
    case "Sunday":
        print(7)
    case _:
        print("Invalid day")


operation=2
match operation:
    case 1:
        print("Check balance")
    case 2:
        print("Withdraw money")
    case 3:
        print("Deposit money")
    case 4:
        print("Exit")
    case _:
        print("Invalid option")'''

# Task
'''category=int(input("Enter choice"))
match category:
    case 1:
        print("You selected Pizza-10$")
    case 2:
        print("You selected Burger-8$")
    case 3:
        print("You selected Biryani-5$")
    case 4:
        print("You selected Dosa-0.2$")
    case _:
        print("Invalid order")'''
            

#List
'''l1=[1,3.14,"hello",True]
print(l1)
l2=[2,"abcd",2.98,False,3,5]
print(l2)
a=3
b=4.14
l3=[a,b]
print(l3)
c,d=3,4
l4=[c]
print(l4)
print(l1[-1])

l1=['😊','😂','😁']
print(l1)'''

#Range
'''print(list(range(1,10)))
print(list(range(10)))
print(list(range(1,10,2)))
print(list(range(4,20,3)))
print(list(range(10,1,-3)))
print(list(range(40,2,-6)))'''

'''options=4
match options:
    case 1:
        print("View marks")
    case 2:
        print("View attendance")
    case 3:
        print("View timetable")
    case 4:
        print("View fee details")
    case _:
        print("Invalid option")'''

#Loops
'''for i in range(1,41):
    print(5*i)
for i in range(1,21):
    print(7,'*',i,'=',7*i)

sum=0
for i in range(1,11):
    sum=sum+i
print("sum is:",sum)

sum=0
for i in range(0,51,2):
    sum=sum+i
print("sum is:",sum)

sum=0
for i in range(0,51,1):
    if i%2==0:
        sum=sum+i
print(sum)

count=0
for i in range(1,51):
    if i%2==0:
        count=count+1
print(count)

fact=1
for i in range(5,0):
    fact=fact*i
print(fact)

fact=1
n=int(input("enter n"))
for i in range(1,n+1):
    fact=fact*i
print(fact)'''

'''count=1
while count<=5:
    print(count)
    count+=1

count=10
while count>=1:
    print(count)
    count-=1

count=0
while count<=50:
    if count%2==0:
        print(count)
    count+=1

count=1
while count<=50:
    if count%2!=0:
        print(count)
    count+=1

n=7789
while n>0:
    rem=n%10
    print(rem,end=',')
    n=n//10
    


n=7789
count=0
while n>0:
    n=n//10
    count=count+1
print(count)


#Reverse a number
rev=0
n=7789
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)'''


#Palindromes
'''n=121
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if temp==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

n=7789
rev=0
a=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if a==rev:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#Factors of a number
'''n=24
for i in range(1,n+1):
    if n%i==0:
        print(i)

n=24
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1'''

#Perfect number
#Count no.of factors for a given number
#N=7789,7+7+8+9=31

#Patterns
'''n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print(end="\n")

n=5
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print(end="\n")

n=5
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end="")
    print(end="\n")

n=10
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print(end="\n")

n=10
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end="")
    print(end="\n")

n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()

n=5
for i in range(n-1,-1,-1):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()

n=5
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

n=5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
 
n=5
a=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a+1,end=" ")
        a=a+1
    print()'''

#Unconditional statements
#break
'''for i in range(0,10):
    if i==5:
        break
    print(i)

for i in range(0,10):
    break
print(i)'''
#continue
'''for i in range(0,10):
    if i==5:
        continue
    print(i)

for i in range(0,10):
    if i%2==0:
        continue
    print(i)'''
#pass
'''for i in range(3):
    pass

for i in range(0,10):
    pass'''















    
    






























    





















