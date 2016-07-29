class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        if l<2:
            return nums
        i,j = 0,1
        while j<l:
            if not nums[i] and nums[j]:
                nums[i] = nums[j]
                nums[j] = 0
                i+=1
                j+=1
            elif not nums[i] and not nums[j]:
                j+=1
            else:
                i+=1
                j+=1
        return nums





s = Solution()
assert [] == s.moveZeroes([])
assert [1,1,2,4,0,0] == s.moveZeroes([1,0,1,0,2,4])
assert [6,4,5,4,5,6,0,0,0] == s.moveZeroes([0,6,0,4,5,4,5,6,0])
