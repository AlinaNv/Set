res=[]
n=input()
n=input()
for a in n.split():
    p=0
    for i in res:
        if i==a:
            p=1
            break
    if p==0:
        res+=[a]
print(len(res))