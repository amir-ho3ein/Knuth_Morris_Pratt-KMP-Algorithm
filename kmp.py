i, j, pattern_num, text, pattern  = 0, 1, [0], list(input().strip(' ')), list(input().strip(' '))
while j!=len(pattern):
    if (pattern[i]==pattern[j]):
        pattern_num.append(i+1)
        i+=1
        j+=1
    else:
        if (i==0):
            pattern_num.append(0)
            j+=1
        else:
            i=pattern_num[i-1]
i, j = 0, 0

while i<len(text) and j<len(pattern):
    if (text[i]==pattern[j]):
        j+=1
        i+=1
    else:
        if (j==0):
            i+=1
        j=pattern_num[j-1]
print((i-j,i) if j!=0 else "not match!")