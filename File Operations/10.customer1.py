f=open("C:/Users/Ayisha Ziba PT/Desktop/customer","r")
for i in f :
    data=i.rstrip("\n").split(",")
    country=data[-1]
    if (country == "india"):
        print(data[1:5])
