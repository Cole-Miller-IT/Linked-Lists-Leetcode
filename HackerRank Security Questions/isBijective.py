def isBijective(n, myList):
    #print(n)
    #print(myList)
    
    # Check one-to-one (injective)
    oneToOne = True
    seen = set()
    for value in myList:
        if value in seen:
            oneToOne = False
            break
        seen.add(value)
    
    # Check onto (surjective)
    onto = True
    range_set = set(range(1, n))  # {1, 2, ..., n-1}
    for value in range_set:
        if value not in myList:
            onto = False
            break
    
    # Bijective if the function is both one-to-one and onto
    if onto and oneToOne:
        return "YES"
    else:
        return "NO"

# Test the function
n = int(input())
myList = list(map(int, input().split()))

print(isBijective(n, myList))
