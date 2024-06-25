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
            
            #Start at the last value and go to the start until a value is found that isn't the one being removed
            searching = True
            while(searching):
                #whole array contains the removed value
                if lastI < 0:
                    searching = False
                    return 0

                if nums[lastI] != val:
                    break

                lastI -= 1
                newLength -= 1

            while(searching):
                print("======================================")
                print("curI " + str(curI))
                print("lastI " + str(lastI))
                print("newLength " + str(newLength))

                if nums[curI] == val:
                    print("swap before")
                    print(nums)
                    #swap it with the last item
                    nums[curI], nums[lastI] = nums[lastI], nums[curI]

                    print("swap after")
                    print(nums)

                    lastI -= 1
                    newLength -= 1

                if curI >= lastI:
                    print("break")
                    print(nums)
                    searching = False
                    break

                curI += 1

            print(nums)
            print(newLength)
            return newLength