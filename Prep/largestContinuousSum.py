#To find largest Continuous sum and also to keep track of its indexing
def lcs(nums):
    if len(nums)==0: return 0
    max_sum= cur_sum = nums[0]
    st=0
    end=1
    for x in range(1, len(nums)):
        if cur_sum+nums[x]>=nums[x]:
            cur_sum = cur_sum+nums[x]
        else:
            st = x
        if cur_sum>max_sum:
            max_sum= cur_sum
            end=x
    return (max_sum, st, end)

nums = [1,5,-2,5,7,-6,8,3,9,-6,1]
print(lcs(nums))
