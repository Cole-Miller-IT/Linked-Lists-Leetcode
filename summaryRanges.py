class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        if len(nums) == 0:
            return ranges

        elif len(nums) == 1:
            #add the one range to ranges
            ranges.append(str(nums[0]))
            return ranges

        #Two or more numbers
        else:
            a = None
            b = None 
            #While going through the nums array
            index = 0
            for num in nums:
                #print("---------")
                #print("current num: " + str(num))
                #print("current ranges: " + str(ranges))
                #print("a: " + str(a))
                #print("b: " + str(b))

                if a == None:
                    a = num

                if b == None:
                    b = num

                if index == 0:
                    index += 1
                    continue

                else:
                    index += 1
                    #check current num against range
                    if num > (b + 1):
                        #range is not contiguous. 
                        #Add the current range
                        if a == b:
                            ranges.append(str(a))

                        else:
                            newRange = str(a) + "->" + str(b)
                            ranges.append(newRange)
                        
                        #create a new range
                        a = num
                        b = num

                        #if this is the last number
                        if index == (len(nums)):
                            #Add the current range
                            ranges.append(str(a))

                    else:
                        #range is contiguous.
                        #print("contig")
                        b = num

                        if index == (len(nums)):
                            #Add the current range
                            if a == b:
                                ranges.append(str(a))
                            
                            else:
                                newRange = str(a) + "->" + str(b)
                                ranges.append(newRange)

            #print("final range: " + str(ranges))
            return ranges

        