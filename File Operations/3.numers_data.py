lst=[] #create a empty list
f=open('numbers','r')
for i in f :
    lst.append(int(i)) #ella num new listil append cheythu
print(sum(lst))