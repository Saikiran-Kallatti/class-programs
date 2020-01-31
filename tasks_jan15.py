'''a = "hello"
b = "world"
print(a+"_"+b)'''

'''s = input()
a = s[0].upper()
b = s[-1].upper()
#print(a)
#print(b)
op = s.replace(s[0],a)
op = op.replace(op[-1],b)
print(op)'''


'''s = input()
a = s[0].upper()
b = s[-1].upper()
print(a+s[1:-1])+b'''


a = input()
b = input()
c = a+b
d = len(c)
e = d//2
f = c[e].upper()
#print(f)
print(c[:e]+f+c[e+1:])
