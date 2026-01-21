n=[2,3,4]
target=6
def check(n,target):
    i=0
    while target-n[i] not in n:
        i+=1
    return [i+1,n.index(target-n[i])+1]

print(check(n,target))


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    1, r = 0, len(numbers) - 1

    while 1 < r:
        curSum = numbers[1] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            1 += 1
        else:
            return [1 + 1, r + 1]