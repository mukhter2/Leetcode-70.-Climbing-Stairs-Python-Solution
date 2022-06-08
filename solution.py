class Solution:
    def climbStairs(self, n: int) -> int:
        lstfin=[0]*(n+1)
        def recursivefunc(n):
            if n<=1:
                return 1
            else:
                if lstfin[n-1]==0:
                    lstfin[n-1] = recursivefunc(n-1)
                if lstfin[n-2]==0:
                    lstfin[n-2]= recursivefunc(n-2)

                return lstfin[n-1]+lstfin[n-2]
    
        x=recursivefunc(n)
        return x
