'''
create a empty list
ass -1 at position 0
ass 3 at the end
add [-1,-2,]'''

li1 = []
li1.insert(0,-1)
print(li1)
li1.append(3)
print(li1)
li1 = li1 + [-1,-2,-3,0,1,4,5,8]
print(li1)
print(li1.count(-1))
li1.extend([0,-9,9])
summ = sum(li1)
print(summ)

length = len(li1)
print(length)
mean = summ/length
print("mean = ", mean)


#print median, second lowest, middle element
