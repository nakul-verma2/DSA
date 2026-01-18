# def check(nums):
#         for i in nums:
#             find=i
#             nums.remove(i)
#             if find in nums:
#                 return True
#         return False

# def check(nums):
#     # We loop over a copy (nums[:]) so the original list 
#     # can be modified safely.
#     for i in nums[:]: 
#         find = i
#         nums.remove(i)
#         if find in nums:
#             return True
#     return False

# optimal solution
def check(num):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False


#best solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         num1=set(nums)
#         if len(num1) == len(nums):
#             return False
#         else:
#             return True
nums = [274, -735, -911, 80, 454, -511, 922, -775, 985, -669, -463, -896, -629, -586, 910, -361, 288, -375, 88, 556, -578, -406, -87, 25, 377, -635, -445, -289, 646, -962, -487, -924, -968, -962, 502, 36, 129, -611, 54, -27, -496, 915, -84, -782, 349, 678, 332, -114, 345, 14, 119, 710, 821, -194, 988, 38, -369, 409, -559, -529, -298, -593, 705]
print(check(nums)) # Now returns True