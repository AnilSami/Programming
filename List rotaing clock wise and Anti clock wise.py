n = 4
l = []
pos = "-"
rot = 3
for i in range(n+1) :
    l.append(i+1)
if pos == "+" :
    while rot!=0 :
        temp = 0
        i = 0
        while True :
            if i == 0 :
                temp = l[0]
            l[i] = l[i+1]
            i+=1
            if i==n :
                l[i] = temp
                print(*l)
                break
        rot-=1
elif pos == "-" :
    while rot!=0 :
        temp = 0
        i = 0
        while True :
            if i == 0 :
                temp = l[n]
            l[n-i] = l[n-i-1]
            i+=1
            if i == n :
                l[0] = temp
                break
        rot-=1
print(l)