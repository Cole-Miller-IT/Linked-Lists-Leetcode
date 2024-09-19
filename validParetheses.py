class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #Yes it's a list, but we'll treat it like a stack  

        if len(s) == 0:
            return False

        if len(s) % 2 == 1: #odd amount of characters
            return False

        else: #even amount of characters
            for char in s:
                #print("Stack: " + str(stack))
                #print(char)

                #If opening bracket
                if (char == '(' or char == '{' or char == '['):
                    #Add to stack
                    stack.append(char)

                #Closing bracket
                else: 
                    #Remove the top of the stack and compare it with the current char
                    if len(stack) == 0:
                        return False

                    else:
                        top = stack.pop()
                        #print("Compare: ")
                        #print("Top: " + str(top))
                        #print("Char: " + str(char))

                        if top == '(':
                            #print("(")
                            if char != ')':
                                return False

                        elif top == '{':
                            #print("{")
                            if char != '}':
                                return False

                        else: #top == '['
                            #print("[")
                            if char != ']':
                                return False

            #check if the stack is empty
            if len(stack) > 0:
                return False

            else:
                return True