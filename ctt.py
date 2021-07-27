
import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    al,bo=0,0
    for i in range(3):
        if(a[i]>b[i]):
            al+=1
        elif(b[i]>a[i]):
            bo+=1
            
    res=[al, bo]
    return(res)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
