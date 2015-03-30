
def sumOfFactorial(n):
    list1 = []
    list1.append(n)
    while n > 1:
        n = n - 1
        list1.append(n)
    print list1
    newnumber = 1
    for number in list1:
            newnumber *= number
    newnumber = str(newnumber)
    length = len(str(newnumber))    
    list1 = []
    for n in newnumber[0:length+1:1]:
        list1.append(int(n))
    print sum(list1)

    
        
        
        
 
