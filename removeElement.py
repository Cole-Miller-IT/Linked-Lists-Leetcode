#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLength = len(nums)

        if numsLength == 0:
            return 0
        
        elif numsLength == 1:
            if nums[0] == val:
                return 0

            else:
                return 1
        
        else: #numsLength >= 2
            curI = 0
            lastI = numsLength - 1
            newLength = numsLength
            
            searching = True
            while(searching):
                #if last value is equal to val
                if nums[lastI] == val:
                    #check if curI and lastI are at the same index
                    if lastI == curI:
                        #print("gone through the whole array")
                        searching = False
                        return curI

                    #print(str(nums[lastI]) + " equal to val, decreasing lastI")
                    lastI -= 1

                else:
                    #check if nums[curI] is equal to val
                    if nums[curI] == val:
                        #print("yes, swap with the last value")
                        nums[curI], nums[lastI] = nums[lastI], nums[curI]

                        #increment one of the indexes and check if the indices are now equal
                        curI += 1
                        if curI == lastI:
                            #print("end of array")
                            searching = False
                            return curI

                        else:
                            #increment the other index after confiming that they are not equal. 
                            #i.e. more of the array to check
                            lastI -= 1

                    else:
                        #print("no")
                        #check if curI and lastI are at the same index
                        if lastI == curI:
                            #print("gone through the whole array 2")
                            searching = False
                            return curI + 1

                        else:
                            #print("increment curI")
                            curI += 1
            