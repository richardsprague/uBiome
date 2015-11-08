__author__ = 'sprague'

ecology = [("apples",3), ("bananas",2), ("carrot",1)]

eT, eN =  list(zip(*ecology))

for i,j in enumerate(eT):
    print(eN[i]*(eN[i]-1))
    print("--",i)


t = sum(eN)*(sum(eN)-1)
print(t)

u =[eN[i]*(eN[i]-1) for i,j in enumerate(eN)]

d = 1- sum([eN[i]*(eN[i]-1) for i,j in enumerate(eN)])/(sum(eN)*(sum(eN)-1))
