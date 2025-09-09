import math
class Solution:
    def isPrime(self, n):
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    def exactly3Divisors(self,N):
        # code here
        count = 0
        for i in range(2, math.floor(math.sqrt(N))+1):
            if self.isPrime(i):
                count+=1
        return count


obj = Solution()
print(obj.exactly3Divisors(49))