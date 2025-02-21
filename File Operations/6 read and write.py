f=open("data","r")
f1=open("data_write","w")  #here the new file will create itself ,
                       # so no need of create a new file
for i in f:
    f1.write(i)