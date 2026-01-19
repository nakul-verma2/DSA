s="A man, a plan, a canal: Panama"
def check(s):
    for i in s:
        if not i.isalnum():
            s = s.replace(i,"")
    r = s[::-1]
    
    if s.lower() == r.lower():
        return True
    else:
        return False
check(s)