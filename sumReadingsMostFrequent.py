def solution(readings):
    def reduce(num):
        result = 0
        for char in num:
            #print(char)
            result += int(char)
            
        #print(result)
        return result
    
    
    #print(readings)
    
    reducing = True
    while(reducing):
        #print("----------------------")
        index = 0
        for num in readings:
            #print("*********")
            #print(num)
            
            num = str(num)
            if len(num) > 1:
                #print('reduce')
                readings[index] = reduce(num)
                reducing = True
                
            else:
                
                reducing = False
                
            index += 1
                
                
    #print(readings)
    
    #Count each digit, store in dictionary
    countDict = {}
    for num in readings:
        print(num)
        
        if countDict.get(num) == None:
            #first time
            countDict[num] = 1
            
        else:
            #2 or more
            countDict.update({num: countDict.get(num) + 1})
    
    print(countDict)
    
    #go through and see what is the most freq. number
    mostFreqNum = 0
    freq = 0
    for num in countDict:
        print(num)
        print(countDict[num])
        
        if countDict[num] > freq:   
            mostFreqNum = num
            freq = countDict[num]
            
        if countDict[num] == freq:
            #determine if it is higher
            if num > mostFreqNum:
                mostFreqNum = num
                freq = countDict[num]
                
            #else: leave it the same
            
    return mostFreqNum
    
    

