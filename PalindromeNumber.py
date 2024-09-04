#this program finds palindrome numbers 
# and returns true if the given number is a palindrome

class Solution:
    def isPalindrome(self, x:int) -> bool:
        lis = list(str(x)) #convert int to string and then string to list
        secondList = [] #empty list for reversed list
        for num in reversed(lis): #reversed() method parses through a list in reversed order
            secondList.append(num)
        if lis == secondList:
            print("True")
            print(lis)
            print(secondList)
            return True
        else:
            print("False")
            return False

solutionInstance = Solution()
solutionInstance.isPalindrome(150)