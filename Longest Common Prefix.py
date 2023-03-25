Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        curr_min = len(strs[0])
        for i in range(1, len(strs)):
            curr_min = min(curr_min,len(strs[i]))
        
        res = ''
        pos = 0

        while pos < curr_min:
            curr_word = strs[0][pos]
            for j in range(1, len(strs)):
                if strs[j][pos] != curr_word:
                    return res
            res += curr_word
            pos += 1
        return res
