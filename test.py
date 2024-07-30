class Solution:
    def strtoint(self, str_):
        n = len(str_) - 1
        num = 0
        for i in str_:
            num += (ord(i) - ord('0')) * 10**n
            n -= 1
        return num
        
    def multiply(self, num1: str, num2: str) -> str:
        num1_ = self.strtoint(num1)
        num2_ = self.strtoint(num2)

        res = num1_ * num2_
        
        ans = ''
        while(res):
            ans += chr(ord('0') + int(res % 10))
            res //= 10

        return ans[::-1]
solution = Solution().multiply('0', '1')
print(solution)
        