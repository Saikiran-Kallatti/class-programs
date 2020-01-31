#program to print the following pattern

#for x in range()


'''#read the number of inputs from the user
n = int(input("enter the range:"))
a = []
for n in range(n):
    s = input()
    a.append(s)
print(a)'''

'''
r = int(input())

for r in range (1,r+1):
    if (r % 3 == 0) and (r % 5== 0):
        print( r , ": fiss and buzz")
    elif (r % 3 == 0):
        print(r,": fiss")
    elif(r % 5 == 0):
        print(r,": buzz")
    else:
        print(r,": NA")
'''

n = int(input("enter the range:"))
a = {}
flag = 0
i = 1
while (flag != 1):
    k = int(input("enter the key: "))
    v = input("enter the value :")

    if len(list(a.keys())==0):
        a[k] = v

    if k in a:
        print("key already exists,  kindly enter distinct key")
        continue;

    a[k] = v


print(a)
