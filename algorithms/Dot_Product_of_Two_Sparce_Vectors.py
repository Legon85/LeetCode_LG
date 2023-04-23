class SparseVector:
    def __init__(self, nums: list[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vec = v2
        return sum([self.nums[i] * vec.nums[i] for i in range(len(self.nums))])


v1 = SparseVector([1, 0, 0, 2, 3])
v2 = SparseVector([0, 3, 0, 4, 0])
ans = v1.dotProduct(v2)
print(ans)

v1 = SparseVector([0, 1, 0, 0, 0])
v2 = SparseVector([0, 0, 0, 0, 2])
ans = v1.dotProduct(v2)
print(ans)

