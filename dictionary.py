val1 = {1 : "maths",2:"statistics",3:"game theory", 4:"DBMS"}
print(val1)
print(val1[5])
print(val1[1])

#add/replace
print(type(val1))
print(len(val1))
print(val1".keys())
print(val1.values())
print(val1.items())

val1[5] = "os"
val1[6] = "nwing"
print(val1)
val1[4] = "mining"
print(val1)
print(val1.get(3))

#update
val2 = {9:"grapics", 10:"java"}
val1 = val1.update(val2)
print(val1)

print(val1)
