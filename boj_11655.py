text = list(input())
ans = []
for each in text:
    if 65 <= ord(each) <= 90:
        aski = ord(each) + 13
        if aski > 90:
            aski = aski - 90 + 64
        alpha = chr(aski)
        ans.append(alpha)
    elif 97 <= ord(each) <= 122:
        aski = ord(each) + 13
        if aski > 122:
            aski = aski - 122 + 96
        alpha = chr(aski)
        ans.append(alpha)
    elif 48 <= ord(each) <= 57:
        ans.append(each)
    else:
        ans.append(each)
        
print(*ans, sep='')
