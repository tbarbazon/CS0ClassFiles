import time
start = time.time()
factors = [11,13,14,16,17,18,19,20]
for possibility in xrange(2520, 300000000, 2520):
    if all(possibility % factor == 0 for factor in factors):
        print possibility
        break
                    
end = time.time() - start
print end
         