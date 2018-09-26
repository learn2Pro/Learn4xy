# 1 2 3
# | | |
arr = [1, 2, 3]
stepNum = 0


def Hanoi(n, start, end):
    if (n == 1):
        print(str(start) + "->" + str(end))
    else:
        endIdx = arr.index(end)
        startIdx = arr.index(start)
        otherIdx = 3 - endIdx - startIdx
        Hanoi(n - 1, start, arr[otherIdx])
        print(str(start) + "->" + str(end))
        Hanoi(n - 1, arr[otherIdx], end)

def Fib(n):
   if(n == 0 or n == 1):
       return n
   else :
       return Fib(n - 1) + Fib(n - 2)

print "fib is :"+str(Fib(20))

#
# Hanoi(4, 1, 3)

# print("1->2")
