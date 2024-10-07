class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b =="0":
            return "0"

        elif a != "0" and b == "0":
            return a

        elif a == "0" and b != "0":
            return b

        else:
            #print("a: "+ str(a))
            #print("b: " + str(b))

            aIndex = len(a) - 1
            bIndex = len(b) - 1
            #print(aIndex)
            #print(bIndex)

            remainder = 0
            aVal = 0
            bVal = 0
            returnString = ""
            summing = True
            while(summing):
                #print("------------")
                #print("returnString: " + str(returnString))
                if aIndex >= 0:
                    aVal = int(a[aIndex])
                else:
                    aVal = 0

                if bIndex >= 0:
                    bVal = int(b[bIndex])
                else:
                    bVal = 0

                result = aVal + bVal + remainder


                #print("calc: " + str(result))
                #print("remainder: " + str(remainder))
                

                if result == 0:
                    returnString += "0"

                elif result == 1:
                    returnString += "1"
                    remainder = 0

                else:
                    #print("deal with remainder")
                    if result == 2:
                        remainder = 1
                        returnString += "0"

                    if result == 3:
                        remainder = 1
                        returnString += "1"


                aIndex -= 1
                bIndex -= 1

                #if gone through both strings
                if aIndex < 0 and bIndex < 0:
                    summing = False
                    if remainder == 1:
                        returnString += "1"

            return returnString[::-1] #Reverse the order of the string and return it
        