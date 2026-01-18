nums = [2,7,11,15]
target = 9

def check(nums, target):
    # solution didnt worked
    # for i in nums:
    #     if i>=target:
    #         p=nums.index(i)
    #         nums=nums[0:p]
    #         break
    # for i in nums:
    #     for j in nums:
    #         if(i==j):
    #             pass
    #         elif i+j==target:
    #             return nums.index(i),nums.index(j)
            
    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
check(nums,target)