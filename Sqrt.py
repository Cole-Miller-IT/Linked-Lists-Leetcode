class Solution:
    def mySqrt(self, x: int) -> int:
        #print(x)

        if x < 0:
            raise ValueError("x must be a non-negative integer")

        if x == 0 or x == 1:
            return x

        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            # If mid*mid == x, mid is the square root
            if mid * mid == x:
                result = mid
                break
            # If mid*mid is less than x, move the left bound up
            elif mid * mid < x:
                result = mid  # store the result as we want the floor of sqrt
                left = mid + 1
            # If mid*mid is greater than x, move the right bound down
            else:
                right = mid - 1


        #round it down
        result = math.floor(result)

        #turn it to an absolute value
        result = abs(result)

        return result
        