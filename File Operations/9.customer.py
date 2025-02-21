f=open("C:/Users/Ayisha Ziba PT/Desktop/customer","r")
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[-3]
    if (age>"40"):
        print(data[1:5])

#if age>40-----> fname,lname , age,prof