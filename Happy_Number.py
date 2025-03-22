'''
Happy Number - 

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
def fn(s) :
    dig = 0
    while s!=0 :
        dig+=(s%10)*(s%10)
        s=s//10
    return dig
def hp(n) :
    vis = [n]
    p = 0
    if n == 1 :
        return True
    while True :
         p = fn(n)
         if p in vis :
             break
         if p == 1 :
             return True
         vis.append(p)
         n = p
    print(vis)
    if p!=1 :
        return False
        
n = int(input())
flg = hp(n)
if flg :
    print("Happy Number")
else :
    print("Not a Happy Number")
