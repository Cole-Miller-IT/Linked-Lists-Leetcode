class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #print("nums: " + str(nums))

        prevNum = None
        frequency = 0
        k = len(nums)
        index = 0
        for curNum in nums:
            #print("---------")
            #print("num: " + str(curNum))

            if prevNum == curNum:
                #not the first time seeing this number
                frequency += 1

                if frequency >= 3:
                    k -= 1

                    #set the value to the max value of a 32 bit int
                    nums[index] = sys.maxsize
            else:
                #first time seeing this value
                prevNum = curNum
                frequency = 1

            index += 1


        #sort the array in ascending order
        #the other values that we swapped to the max values will be sorted to the end of the array
        #print("before sort: " + str(nums))
        nums.sort()
        #print("after sort: " + str(nums))
        #print("k: " + str(k))
        
        return k
        