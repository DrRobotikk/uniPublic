#Program for å slå sammen to lister til en etter gitt kriterie

#L1 og L2 defineres
l1=[1,14,26,37,100,86,77,99]
l2=[2,13,27,30,99,85,78,106,4,47,56]
nyliste=[]

#Utskrift før sammenslåing
print(l1)
print(l2)
print(nyliste)
print()

liste_lengde_l1=len(l1)
liste_lengde_l2=len(l2)

for n in range(0,liste_lengde_l1,1):
    nyliste+= [l1[n]]

for n in range(0,liste_lengde_l2,1):
    nyliste+=[l2[n]]

#Printer liste etter sammenslåing
print(nyliste)
