def valied(i) :
    return (i>=0 and i<len(s))
def LPS(text) :
    lps = text[0]
    for i in range(len(text)) :
        if valied(i+1) and valied(i-1):
            if text[i] == text[i+1] :
                c = even(text,i)
                if len(lps) < len(c) :
                    lps = c
            else :
                c = odd(text,i)
                if len(lps) < len(c) :
                    lps = c
        else :
            continue
    return lps
def even(text,i) :
    st,ed = i,i+1
    new = ""
    while True :
        if valied(st) and valied(ed) :
            if text[st] == text[ed] :
                new = text[st] + new + text[ed]
                st-=1
                ed+=1
            else :
                break
        else :
            break
    return new
def odd(text,i) :
    st,ed = i-1,i+1
    new = text[i]
    while True :
        if valied(st) and valied(ed) :
            if text[st] == text[ed] :
                new = text[st] + new + text[ed]
                st-=1
                ed+=1
            else :
                break
        else :
            break
    return new
#Input 1  --> s = "aaaabc"
#Output 1 --> aaaa
#Input 2  --> s = "forgeeksskeegfor"
#Output 2 --> geeksskeeg
#Input 3 --> s = "ababd"
#Output 2 --> bab
#Input 4 --> s = "abc"
#Output 4 --> a
#Input 5 --> s = "Geeks"
#Output 5 --> ee

s = input()

print(LPS(s))
