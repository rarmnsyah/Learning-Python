class Solution:
    def matrixSum(self, nums) -> int:
        tempScore = [max(j.pop(j.index(max(j))) for j in nums) for _ in range(len(nums[0]))]
        # print([max(j.pop(j.index(max(j))) for j in nums) for _ in range(len(nums[0]))])
        print(tempScore)
        return sum(tempScore)
    
m, n = map(int, input().split())
val = []
for i in range(m):
    val.append(list(map(int, input().split())))

solusi = Solution()
print(solusi.matrixSum(val))
# print(solusi.matrixSum([[86, 46], [88, 5], [57, 71]]))