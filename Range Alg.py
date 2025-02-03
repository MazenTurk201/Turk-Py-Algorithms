def rangee(to=0,fromm=-1,stepp=1):
    lest=[]
    x=fromm
    lest.append(x)
    while x <= to-1:
        x+=stepp
        lest.append(x)
    return lest

for i in range(5,19,2):
    print(i,end=" ")
print()
for i in rangee(19,5,2):
    print(i,end=" ")