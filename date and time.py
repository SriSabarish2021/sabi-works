import datetime as dtsa
today = dtsa.date.today()
print("today date is : ", today)

new1= dtsa.date(2021,12,15)
print("my year : ",new1)

print("my day :" , new1.day)
print("my year : ", new1.year)
print("my month : ", new1.month)

a = dtsa.time(11,45,50,55)
print(a)
print(a.minute)
print(a.second)
print(a.hour)

ippo=dtsa.datetime.now()
print( "current date and timer : ", ippo)

new=dtsa.datetime(2022,5,12,1,30,40,555)
print("my first :" , new)
print(new.year)
print(new.day)
print(new.minute)
print(new.second)
print(new.date())

current=dtsa.datetime.now()
next_myday=dtsa.datetime(2024,5,12)
mine=current-next_myday
print("waiting :", mine)

amine=ippo.strftime("%a %A %b")
print(amine)
