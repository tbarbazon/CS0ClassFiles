def problem():
    list1 = []
    for number in range(2, 101):
        for number2 in range(2, 101):
            ans3 = number**number2
            if list1.count(ans3) == 0:
                list1.append(ans3) 
    print len(sorted(list1))
problem()
   
    
    
