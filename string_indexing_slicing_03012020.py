#
'''a = "python"
print(a)
print(a[5])  #printing last letter using forwafrd indexing
print(a[-1]) #printing last letter using reverse indexing
print(len(a)) #print length of the string'''

#read string and print the middle charecter of the string
'''a = input("eneter the string : ")
print(len(a))
b = len(a) - 1
c = int(b/2)          #alternatively floor division can be used here as b//2
d = a[c]
print(d)'''

#alternative to above pgm
'''a = input("eneter the string : ")
print(a[len(a)//2])
print(a[-2])'''

a = input("eneter the string : ")
print(a[0:3])
print(a[-6:-3])
