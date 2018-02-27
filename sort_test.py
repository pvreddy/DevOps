list1 = [8,3,5,1,2,9,4]
new_l = []

while list1:
    minimum = list1[0]
    for x in list1:
        if x < minimum:
            minimum = x
    new_l.append(minimum)
    list1.remove(minimum)

print new_l
    
