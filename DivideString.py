class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        string_length = len(s)
        temp = []

        if string_length % k == 0:
            for i in range(0,string_length,k):
                temp.append(s[i:i+k])
        else:
            for i in range(0, string_length, k):
                temp.append(s[i:i+k])
            if len(temp[-1]) != k:
                amount_needed = k - len(temp[-1])
                temp[-1] += (str(fill) * (amount_needed))
        return temp
