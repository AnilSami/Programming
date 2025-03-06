d = []
name1 = "ABCD"
name2 = "ABCDAC"
def fill(text) :
    for i in text :
        d.append(i)
    return d
def imp(text,l) :
    vis = []
    for i in text :
        if ( i in d ) and (i not in vis):
            vis.append(i)
            d.remove(i)
        else :
            d.append(i)
    return d

def check(fl) :
    c = 0
    for i in fl :
        if i != "X" :
            c+=1
    if c == 1 :
        return False
    else :
        return True
   
flames = ["F","L","A","M","E","S"]
name1 = fill(name1)
name2 = imp(name2,name1)
count = len(name2)
i = 0
piv = 0
tp = 0
while check(flames) :
    if i == (count-1) and flames[piv]!='X':
        flames[piv] = 'X'
        i = 0
        tp+=1
    if flames[piv]=='X' :
        piv+=1
        if piv == len(flames) :
            piv = 0
        continue
    i+=1    
    piv+=1
    if piv == len(flames) :
        piv = 0
print(flames)
    












