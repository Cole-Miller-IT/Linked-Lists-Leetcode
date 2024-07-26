class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        elif len(nums) == 0:
            return nums[0]

        else: #nums len greater than or equal to 2\
            #hold each unique 
            bins = {}

            for number in nums:
                #print(number)
                #if this is an existing number, increase it
                if number in bins:
                    bins[number] = bins.get(number) + 1

                else:
                    #else, add the number 
                    bins[number] = 1

                
            #print(bins)
            for number in bins:
                #print("Number: " + str(number) + " with occurances: " + str(bins.get(number)))
                if bins.get(number) > ((len(nums) / 2)):
                    #print(str(number) + " is the majority element.")
                    return number
        