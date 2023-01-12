liste=[]
l1=[1,3,5,7]
l2=[2,4,6,8,10]

print(liste)
print(l1)
print(l2)

l1_lengde=len(l1)
l2_lengde=len(l2)

totallengde= l1_lengde + l2_lengde

for n in range(0,totallengde,1):
    if n < l1_lengde:
        liste += [l1[n]]
    if n < l2_lengde:
        liste += [l2[n]]

print(liste)