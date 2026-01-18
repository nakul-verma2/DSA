s="aacc"
t="ccac"
def check(s,t):
    if len(s)!=len(t):
        return False
    s=sorted(s)
    t=sorted(t)
    
    if s==t:
        return True
    else:
        return False
# optimal solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        an=set(t)
        for i in an:
            if s.count(i)!=t.count(i):
                return False
        return True
print(check(s,t))