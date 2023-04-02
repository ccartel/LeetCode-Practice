Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
  
  
import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = string.ascii_uppercase
        d = dict()
        count = 1

        for i in letters:
            d[i] = count
            count +=1
        res = 0
        for k in range (0,len(columnTitle)):
            res = res + d[columnTitle[k]] * (26 ** (len(columnTitle) - 1 - k))

        return res 

        
