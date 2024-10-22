# Enter your code here. Read input from STDIN. Print output to STDOUT
# f(x): X -> Y      inverse to      f-1(x): Y -> X
def inverse(n, myList):
    #print(n)
    #print(myList)
    
    inverseList = [-1 for x in myList]
    for num in range(1, n + 1):
        #print("num: " + str(num))
        #print("f(num) = " + str(myList[num - 1]))
        
        
        #Map the X values to Y values, Store the Y values in order
        inverseList[num - 1] = myList[num - 1]
        #print(inverseList)
        
        
    return inverseList
    

n = int(input())
myList = list(map(int, input().split()))

result = inverse(n, myList)
#print(result)

#The Y values are unsorted, go through the results until you find the first value F-1(1), then F-1(2), etc..
for num in range(1, n + 1):
    #print("num: " + str(num))
    searching = True
    index = 0
    while(searching):
        #if the value in the results matches the current number ie. 1 for F-1(1) then 
        #the index it is stored at will be the X value
        if result[index] == num:
            #print("X value " + str(index + 1))
            print(index + 1)
            searching = False
            break
            
        index += 1






