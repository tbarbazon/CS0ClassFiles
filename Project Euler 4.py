def largestPalindrome():
    import time
    start = time.time()
    largestSoFar = 0
    for number in range(1, 1000):
        for number2 in range (1, 1000):
            numAns = str(number * number2)
            if numAns[::-1] == numAns:
                if int(numAns) > int(largestSoFar):
                    largestSoFar = numAns
    print largestSoFar
    print "Total runtime:  " + str(time.time() - start)
largestPalindrome()
        
        