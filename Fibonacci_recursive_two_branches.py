class Solution:
    def fibonacci_recursive(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)


solucao = Solution()
print(solucao.fibonacci_recursive(10))
