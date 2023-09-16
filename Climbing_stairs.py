# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # base cases: If there are 0 or 1 steps, there is only one way to climb
    def cimbling_stairs(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            # recursive case: counting the ways to climb when taking 1 step or 2 steps
            return self.cimbling_stairs(n - 1) + self.cimbling_stairs(n - 2)


solucao = Solution()
print(solucao.cimbling_stairs(5))