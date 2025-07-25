arr = [1,2,3,4]
r = 3

un = ['x'] * r # ['x','x']
res = []

def comb(arr,un,r):
    for i in range(len(arr)):
        un[len(un)-r] = arr[i]
        if r>1:
            comb(arr[i+1:],un,r-1)
        else:
            print(un)




    

comb(arr,un,r)



