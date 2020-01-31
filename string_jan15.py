a = "hello"
b = "world"
c = a+b
print(c)

a = "hello"
b = a.upper()
print(b)

a = "Hello"
b = a.lower()
print(b)

a = "hello"
b = a.capitalize()
print(b)

a = "HelloWorld"
b = a.swapcase()
print(b)

a = "hello"
print(len(a))
print(type(a))

a = "hello world"
print(a.count("r"))
print(a.count("z"))
print(a.count("l"))
print(a.find("l"))
print(a.find("z"))
print(a.find("e"))


a = "hello_world"
b = a.replace("_","*")
print(b)

a = "hello"
b = a*3
print(b)

a = "_python_"
b = a.lstrip("_")
c = a.rstrip("_")
d = a.strip("_")
print(b)
print(c)
print(d)
