# for a given roman numeral, return the integer equivalent

class Solution:
    def romanToInt(self, s:str) -> int:
        s = list(s) #saves string to list of each character in string
        print(s)
        sum = 0

        #will probably want to catch any leading i's prior to case-matching

        #iterate through every item in the list
        for x in s:
            match x:
                case "i": 
                    print("x is 1")


        return sum
    

solution_instance = Solution()
result = solution_instance.romanToInt("iii")