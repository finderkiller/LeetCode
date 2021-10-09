class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        self.a = a
        self.b = b
        self.c = c
        result = map(self.quadratic, nums)
        return sorted(result)
        
    def quadratic(self, x):
        return self.a*x**2 + self.b*x + self.c