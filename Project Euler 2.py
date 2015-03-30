a = 1 
b = a + a
c = b + a
list1 = []
list1.append(a)
list2 = []
def test(b, c):

    if b < 4000000 or c < 4000000:
        list1.append(b)
        list1.append(c)
        b = b + c
        c = c + b
        test(b, c)
    else:
         print "done"  
test(b,c)    
for x in list1:
    if x > 4000000:
        list1.remove(x)
for x in list1:
    if float(x) % 2 == 0:
        list2.append(x)
print sum(list2)       