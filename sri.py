

'''
m1=int(input("m1 mark : "))
m2=int(input("m2 mark : "))
m3=int(input("m3 mark : " ))
total = m1+m2+m3
average = total / 3.0
print(total)
print(average)
if m1 and m2 and m3 >=35 and m1 and m2 and m3 <=100:
    print("you passes: ")
    if average >90 and average<=100:
        print( "grade: A")
    elif average >80 and average<=89:
        print("grade B")
    elif average >35 and average <=79:
        print("grade : C")
else:
    print("you failed :")
    print (" grade : no grade")


meghna=input("enter the situation :" )
if meghna =='not live':
    print('surya meets priya')
else:
    print('surya weds meghna')

marks=int(input("enter your mark :"))
if marks  >= 35:
    print("you passed")
if marks >= 90 and marks<=100:
        print('grade is A')
if marks >= 80 and  marks<=89:
        print('grade is B')

else:
    print('you fail')
          

a=int(input("A IS :"))
b=int(input("B IS :"))

if a and b ==type(int):
    print('valid')
else:
       print(' not a number')
opt=input("add / sub / muliti / div:")
if opt=='add':
        print(a+b)
elif opt=='sub':
        print(a-b)
elif opt=='muliti':
        print(a*b)
elif opt=='div':
        print(a/b)
else:
    print('not a number')

score=int(input('enter your score :'))
if score >=70:
    print('eligible')
else:
    print('not eligible')

if score >=70:
    a=(input('your name: '))
    b=(input('your dep :'))
    c=input('your location: ')
    print(a)
    print(b)
    print(c)
else:
    print('not a valid person')


a=int(input('marks 1 :'))
b=int(input('marks 2 :'))
c=int(input('marks 3 :'))
d=int(input('marks  4:'))
e=int(input('marks  5:'))

add=(a+b+c+d+e)
print(add)
average=add/5
print(average)
if average >=35:
    print('you are good')
else:
    print('you are bad')

a=int(input('enter a value for a:'))
b=int(input('enter a value for b:'))
for i in range(1,11):
    print(i*2)


for sabi in range(1,11):
    print(sabi,'X2=',sabi*2)

a=int(input("enter the number for A :"))
b=int(input("enter the number for B :"))
for i in range(a+12,b):
    print(i)
o_count=0
e_count=0
for odd in range(1,12):
    if odd%2!=0:
        o_count=o_count+1
    else:
        e_count=e_count+1
print('odd=',o_count)
print('even=',e_count)
   
th_count=0
fv_count=0
for i in range(1,10):
    if i%3==0: 
        th_count=th_count+1
    elif i%5==0:
         fv_count=fv_count+1
print(th_count)
print(fv_count)
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

b=[]
print("enter the first 11 numbers: ")
for a in range(5):
    s=int(input('A is : '+str(a+1)))
    b.append(s)
print(b)
sum=0
for k in b:
    sum=sum+k
print(sum)
1
b=[]
for a in range (1,6):
    s=int(input("your number: "))
    print(s)
    b.append(s)
    if s <=5:
        print(s**3)
    else:
        print('invalid')
 

for i in range (1,3):
    print('WEEK :', i)
    for s in range(1,4):
        print("   Day :",s) 

for s in range(1,6):
    print()
    for a in range (1,s+1):
        print('*',end="") 

for i in range (1,7):
    print()
    for s in range(1,i+1):
        print('*',end="*")


i=4
while 2*2==4:
    print(i)
    i=6

i=10
while i<=10 and i>=1:
    print(i, end="/")
    i=i-1


i=5
while i==5:
    print(i)
    i=6

i=4
sum=1
while i>0:
    sum=sum+i
    i=i-1
print(sum)

i=4
muliti=1
while i>0:
    muliti=muliti*i
    i=i-1
print(muliti)


a=(1,2,3,4,5)
b=[6,7,8,9,0]
c=[6,7,8,9,0]
a1=list(a)
a1.pop(4)
print(a1)
b.pop(2)
print(b)

a={1,2,3,4,5,6}
b={7,8,9,10,11}
a.update(b)
print(a)
a={1,2,3,4,5,6}
a1=list(a)
a1.append(10)
print(a1)

a={"name":"sabi"}
print(a.keys)
print('subtraction')
a=int(input("enter the number :"))
b=int(input("enter another num :"))
def subt():
    print(a-b)



def add():
    print('addition')
    a=int(input("enter the number :"))
    b=int(input("enter another num :"))
    print(a+b)

subt()
add()

def painter(nice):
    print("message :",nice)
painter('mm') 

def find_even_or_odd (msg):
    if a<=35:
        print('fail')
    else:
        print('pass')
a=int(input("enter your mark :"))

find_even_or_odd(a)

def printrange(f,g):
    for i in range(a,b):
       print(i)
a=int(input("enter value A :"))
b=int(input("enter value B :"))
printrange(a,b)



s_username="SRI"
s_password='1'

uname=input("enter your name : ")
password=input("enter your password : ")

def validate():
    if s_username==uname and s_password==password:
        return 'True'
    else:
        return 'false'
    
msg=validate()
print(validate())

a=int(input("enter A : "))
b=int(input("enter B : "))
c=int(input("enter C : "))
def add(a1,b1):
    return a1+b1
added=add(a,b)
output=added*c
print(output)

class goa:
    drink=('enjoy')
    def party():
        print("make fun")
    def beach():
        print('nature')
ramesh=goa 
ramesh.party()

class laptop:
    def __init__(self):
        self.ram=""
        self.price=""
    def sales(self):
        print("your price is :",self.price)
        print("your system ram  is :",self.ram)
hp=laptop()
hp.price='20000'
hp.ram='6gb'
dell=laptop()
dell.ram='12gb'
dell.price='34999'
print('hp')
hp.sales()
print('dell')
dell.sales()

class student():
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("name is :",self.name)
        print("reg no is :",self.regno)

kavin=student()
a=input("your name :")
b=input("your reg no :")
kavin.name=a
kavin.regno=b
mani=student()
s=input("your name 2 :")
r=input("your reg no 2 :")
mani.name=s
mani.regno=r
print("kavin name is :",kavin.name)
print("kavin reg no is : ",kavin.regno)
print("mani name is :",mani.name)
print("mani reg no is : ",mani.regno)
kavin.display()
mani.display()

class fruits():
    def __init__(self,col):
        self.colour=col

appple=fruits('red')
print(appple.colour)

class teacher():
    def __init__(self,n,r):
        self.name=n
        self.regno=r
    def display(self):
        print("Name is :",self.name)
        print("reg no is :",self.regno)
t1=teacher('sri','017')
t2=teacher('sabi','001')
t1.display()
t2.display()

class calculator():
    def __init__(self,a,b):
        self.var1=a
        self.var2=b
    def addition(self):
        print("add is :",self.var1+self.var2)

num1=calculator(10,2)
num1.addition()


class laptop:
    chargertype="c type"
    def __init__(self):
        self.name=''
        self.price="34"
    def setprice (self,price):
        self.price=price
    def getprice(self):
        print("price is :",self.price)
    @staticmethod
    def display():
        print('type is :')
    @classmethod
    def changechargertype(cls):
        cls.chargertype="B type"
        print("charger type is : ",cls.chargertype)
hp=laptop()
hp.setprice('20,000')
hp.getprice()
hp.display()
hp.display()
laptop.changechargertype()

class laptop:
    def name1(self):
        print("dell")

class service(laptop):
    def lapp(self):
        print("good")

class lap(service):
    def name2(self):
        print("azus")

gaming=lap()
gaming.lapp()
'''

class dad():
    def money(self):
        print("needed")
class son1():
    pass
class son2():
    pass
class son3():
    pass

s3=dad()
s3.money()