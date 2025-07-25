def pp(s):
    liste = list(s.lower())
    final=[]
    s2=''
    for i in liste:
        if i.isalnum():
            final.append(i)
    s2= ''.join(final)
    if s2== s2[::-1]:
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"
print(pp(s))

