height=[2,2,2]



def check(heights):
    # res = 0

    # for l in range(len(height)):
    #     for r in range(l +1, len(height)):
    #         area = (r - l) * min(height[l], height[r])
    #         res = max(res, area)
    # return res
    # optimal solution
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - 1) * min(height[1], height[r])
        res = max(res, area)

        if height[1] < height[r]:
            l += 1
        else:
            r -= 1

    return res
print(check(height))