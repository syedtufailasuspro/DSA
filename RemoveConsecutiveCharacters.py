def removeConsecutiveCharacter(S):
    list1 = list(S)
    print(list1)
    for i in range(len(S)-1):
        if list1[i]==list1[i+1]:
            list1[i]=' '
    S = ''.join(list1)
    S=S.replace(' ','')
    return S

print(removeConsecutiveCharacter('a'))