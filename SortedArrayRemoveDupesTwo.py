class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print("nums: " + str(nums))

        prevNum = None
        frequency = 0
        k = len(nums)
        for curNum in nums:
            print("---------")
            print("num: " + str(curNum))

            if prevNum == curNum:
                #not the first time seeing this number
                frequency += 1

                if frequency >= 3:
                    #move the value to the end of the array efficiently




                    #decrement k
                    k -= 1

            else:
                #first time seeing this value
                prevNum = curNum
                frequency = 1
        