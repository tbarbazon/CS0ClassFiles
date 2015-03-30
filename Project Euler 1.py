list1 = []
for multiple in range (2, 1000):
    if multiple % 3 == 0 or multiple % 5 == 0:
       list1.append(multiple)
print sum(list1)
