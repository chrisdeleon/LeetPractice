# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        string = str(x) #converts int to string
        lis = [] # starting list
        resLis = [] # resulting list
        neg = False # holder for negative sign
        for i in string: # convert string to list
            lis.append(i)
        print(lis)
        if lis[0] == "-": # detects negative sign for neg ints
            neg = True
            lis.pop(0) # removes negative sign from list
        for i in reversed(lis): # reverses order of list into a new list
            resLis.append(i)
        if neg: # adds negative sign back if original string was neg
            resLis.insert(0, "-")
        int_result = int(''.join(map(str, resLis))) # converts each item in list of strings into an integer and joins them all
        if int_result > 2147483647  or int_result <  -2147483648: # checks if within specified range
            return 0
        print(int_result)
        return int_result

SolutionInstance = Solution()
result = SolutionInstance.reverse(x = 1534236469)
