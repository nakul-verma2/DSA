nums = [0,1,0,3,12]
def check(nums):
    for i in nums:
        if i ==0:
            nums.remove(0)
            nums.append(0)
    print(nums)
check(nums)

# best solution
# def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n, j = len(nums), -1
#         for i in range(n):
#             if nums[i] == 0:
#                 j = i
#                 break
#         if j != -1:
#             for i in range(j + 1, n):
#                 if nums[i] != 0:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     j += 1