num = [3, 3]
targ = 6

class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                first = nums[i]
                if j != i:
                    if first + nums[j] == target:
                        indices.append(i)
                        indices.append(j)
                        return indices


test = Solution()
sol = test.twoSum(num, targ)
print(sol)