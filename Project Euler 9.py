

import math
#First checks for all odd possibilities using fibonacci's method, then checks using Euclid's method

#K is the starting number and is equal to a^2
for k in xrange(9,1000,2):
    #c is the nth term in the sequence of k
    c = (k+1)/2
    # a is always sqrt of k
    a = math.sqrt(k)
    #checks if a is a whole number, if is continues, if not passes to next k
    if a % 1 == 0:
        #b is n - 1
        b = (c-1)
        if a**2 + b**2 == c**2:
           if a + b + c == 1000:
                print a,b,c
           else:
               #Starts checking with Euclids method.
               for number in xrange(0,1000,2):
                    #Holds all factors and is reasigned for each *number*
                    list1 = []
                    #Finds all factors and appends them to list1
                    for possfactor in xrange(1, number):
                        if number % possfactor == 0:
                            list1.append(possfactor)
                    #goes through all numbers and pairs them up with each other so that it does 2 factors at a time
                    for factor in list1:
                        for factor1 in list1:
                            if factor * factor1 == number:
                                if factor > factor1:
                                    m = factor
                                    n = factor1
                                else:
                                    n = factor
                                    m = factor1
                                    
                                a = (m**2 - n**2)
                                b = 2*(m*n)
                                c = m**2 + n**2
                                #checks conditions via Project Euler.
                                if a**2 + b**2 == c**2:
                                    if a + b + c == 1000:
                                        print a,b,c
                                        
                
    
   
   

    
    
    

                    
    
