class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLength = len(s)

        if sLength == 0:
            return True

        else:
            sIndex = 0
            for character in t:
                #print(character)

                if character == s[sIndex]:
                    #print("matched char")

                    if (sIndex == (sLength - 1)):
                        return True
                    
                    sIndex += 1
                    

            return False
        