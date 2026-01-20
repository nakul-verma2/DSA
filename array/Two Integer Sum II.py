n=[2,3,4]
target=6
def check(n,target):
    i=0
    while target-n[i] not in n:
        i+=1
    return [i+1,n.index(target-n[i])+1]

print(check(n,target))