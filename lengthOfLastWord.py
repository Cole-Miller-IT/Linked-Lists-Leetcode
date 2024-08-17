class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        number = 0
        onlySpacesSoFar = True
        msg = ""

        length = len(s)
        #print(length)

        for c in s:
            #print(s[length - 1])
            character = s[length - 1]

            #Check if the character should be recorded
            if (character == " "):
                #check if we have started recording the last word already
                if (onlySpacesSoFar == True):
                    pass
                else:
                    #We have seen the entire last word
                    number = len(msg)

                    #debugging
                    #msg = msg[::-1]
                    #print(msg)
                   
                    return len(msg)

            #Not a space
            else:
                if (onlySpacesSoFar == True):
                    onlySpacesSoFar = False

                msg = msg + character
                

            length -= 1

        return len(msg)

        