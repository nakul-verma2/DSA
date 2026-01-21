nums=[-1,0,1,2,-1,-4]
def check(nums):
    # my soltution 
    # s = []
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         for k in range(len(nums)):
    #             # Skip if using the same index
    #             if i == j or i == k or j == k:
    #                 continue
                
    #             if (nums[i] + nums[j] + nums[k]) == 0:
    #                 # 1. Create a sorted triplet to handle different orders
    #                 triplet = sorted([nums[i], nums[j], nums[k]])
                    
    #                 # 2. Use 'not in' to check for duplicates correctly
    #                 if triplet not in s:
    #                     s.append(triplet)
    # return s

    
    nums.sort()  # Sort first to use two pointers and handle duplicates
    res = []

    for i in range(len(nums) - 2):
        # 1. Skip the same value for the first number to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # 2. Use two pointers for the remaining two numbers
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # 3. Skip duplicate values for the left pointer
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res

print(check(nums))