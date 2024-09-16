class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapDict = {}
        tIndex = 0
        newS = ""
        tLength = len(t)

        for character in s:
            print(character)
            print(t[tIndex])

            if mapDict.get(character) == None:
                print("first time seeing " + str(character))
                #store the mapping in a dict 
                mapDict[character] = t[tIndex]

                print("new mapping created")
                print(mapDict)
                
                #change s to another value
                newS = newS + mapDict.get(character)

                #Determine the next character for t the s will map to
                #move t index higher until a new character is found
                while(tIndex < tLength):
                    tIndex += 1
                    
                    #fix this
                    if tIndex > tLength:
                        print("at end of string")
                        return False

                    if t[tIndex] != t[tIndex - 1]:
                        break

                    

            else:
                print("Use previous mapping")
                #change s to another value
                newS = newS + mapDict.get(character)


            print("after mapping")
            print(newS)
            print(t)


        #After changing around characters for s
        print("compare")
        print(newS)
        print(t)
        if newS == t:
            return True

        else: 
            return False