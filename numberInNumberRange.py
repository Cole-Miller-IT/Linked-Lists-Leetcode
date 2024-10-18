def solution(numbers, nRange):
    print(numbers)
    print(nRange)
    
    lowestNum = 10000000
    for num in numbers:
        print("-------")
        print(num)
        if (num > nRange[0] and num < nRange[1]):
            print("In range")
            if num <= lowestNum:
                lowestNum = num
            
        else:
            print("out of range")
            
        print("lowestNum: " + str(lowestNum))
        
        
    if lowestNum == 10000000:
        return 0
        
    else:
        return lowestNum
        

