def valied(i,j) :
    return (i>=0 and j>=0) and (i<n and j<n)
def eastw(i,j) :
    if not valied(i,j) or l[i][j] == 'B' :
        return "Done"
    print(l[i][j],end=" ")
    l[i][j] = 'B'
    if valied(i,j+1) and l[i][j+1]!="B" :
        return eastw(i,j+1)
    else :
        return southw(i+1,j)
                
def southw(i,j) :
    if not valied(i,j) or l[i][j] == 'B' :
        return "Done"
    print(l[i][j],end=" ")
    l[i][j]="B"
    if valied(i+1,j) and l[i+1][j]!="B" :
        return southw(i+1,j)
    else :
        return westw(i,j-1)
def westw(i,j) :
    if not valied(i,j) or l[i][j] == 'B' :
        return "Done"
    print(l[i][j],end=" ")
    l[i][j]="B"
    if valied(i,j-1) and l[i][j-1]!="B" :
        return westw(i,j-1)
    else :
        return northw(i-1,j)
def northw(i,j) :
    if not valied(i,j) or l[i][j]=="B" :
        return "Done"
    print(l[i][j],end=" ")
    l[i][j]="B"
    if valied(i-1,j) and l[i-1][j]!="B" :
        return northw(i-1,j)
    else :
        return eastw(i,j+1)

n=int(input("Enter Matrix size :\n"))
row=[]
l=[]
c = 1
for p in range(n) :
    for q in range(n) :
        row.append(c)
        c+=1
    l.append(row)
    row=[]
pos1,pos2 = 0,0
print(eastw(0,0))