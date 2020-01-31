'''tuple1 = (7,8,2,3,4,"python","hi")
print(tuple1)
print(type(tuple1))
print(len(tuple1))
tuple2 = (8.0,7.23,"False","True",9)
print(tuple2)
print(tuple2[2])
print(tuple1[-1])


#concat
tuple3 = tuple1 +tuple2
print(tuple1)
tuple4 = tuple3 + (7,8,9)
print(tuple4)
tuple5 = (2,0,1)+(3,2,4)
print(tuple5)

#multiply
tuple6 = tuple5 * 3
print(tuple6)

#slicing/indexing
tuple7 = tuple6[-8:]
print(tuple7)
tuple8 = tuple7[2:5] + tuple2[1:]
print(tuple8)
'''


'''li1 = [7,8,2,4,3]
li1[-3] = 9
print(li1)
tuple1 = (7,8,2,4,3)
tuple1[-3] = 9
print(tuple1)'''

#Conversion list to tuple
val1 = [7,8,9,-1]
print(val1)
print(type(val1))
val1 = tuple(val1)
print(val1)
print(type(val1))

#tuple yo list
val1 = (9,2,3,4)
print(val1)
print(type(val1))
print(val1)
print(type(val1))
