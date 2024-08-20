class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}

        #store both of the strings in dictionaries
        for char in ransomNote:
            if not char in ransomDict:
                ransomDict[char] = 1
            else:
                ransomDict[char] += 1

        for char in magazine:
            #print(char)
            if not char in magazineDict:
                magazineDict[char] = 1
            else:
                magazineDict[char] += 1

        #print(ransomDict)
        #print(magazineDict)
        #if the magazine has greater or equal charcters to each ransom letter
            #return true

        #go through all the ransom characters
        for character in ransomDict:
            #print(character )
            #print(ransomDict[character])
            
            #check if the value exists in the magazine
            if magazineDict.get(character):
                #print("mag contains " + str(character))
                #check if they exist in equal or greater quantities in the magazine dict
                if magazineDict[character] >= ransomDict[character]:
                    #print("has enough characters")
                    pass

                else:
                    return False

            else:
                return False

        return True
        