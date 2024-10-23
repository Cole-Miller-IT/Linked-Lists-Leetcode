# Enter your code here. Read input from STDIN. Print output to STDOUT


def permutation(n, myList):
    for num in range(0, n):
        #print(num)
        
        result = myFunc(myFunc(num, myList) - 1, myList)
        
        #print("result: " + str(result))
        print(result)
    
    
def myFunc(value, myList):
    return myList[value]
    
n = int(input())
myList = list(map(int, input().split()))

permutation(n, myList)
#print(result)

