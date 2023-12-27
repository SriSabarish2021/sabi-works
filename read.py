'''try:
    file=open("sabarish.py",'w')
    file.write("sabarish")
    file=open("sabarish.py",'r')
    print(file.read())
except FileNotFoundError:
    print("you not have such file")
else:
    quit

n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)'''

a=int(input('enter a value :'))
if a%2==0:
    print('is even')
else:
    print('is odd')