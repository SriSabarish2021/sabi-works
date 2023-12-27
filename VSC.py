a=12
b=15
print(a)
# string and string type 
s= "im sri sabarish"
print(s)
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.count('s'))
print(s.endswith('she'))
print(s.find('sri'))
print(s.find('s' , 4))
print(s.replace('s' , 'a'))
print(s.isupper())
print(s.isdecimal())
print(s.isnumeric())
print(s.isalnum())

a='he \n is \n new'
print(a)
print(s.splitlines())
print(s.strip)
print(s[0:5])
a=4
b=10
print(a==b)
print(a>b)
print(a<=b)
print(a!=b)
print(a)
print(~a)
a=int(input("enter a number :"))
if a%2==0 :
    print(a,"entered number is even")
    a=input("enter your name : ")
    b=int(input("enter your age :"))
    if b>=18:
        print(a,"eligible")
    else:
        print(a, "is not eligible")

days=int(input("enter the days of subb : " ))
if days==0:
    print("good in subb" , days)
elif days >1 and days <=5 :
    print("paid a fain :" , days*2)
elif days >5 and days <=15 :
    print("pain the fain : " , days*4)
else:
    print(days ,"membership cancled")