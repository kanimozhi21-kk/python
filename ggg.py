def readvenuelist():
    dic={}
    venuelist=[]
    open("venue.txt","x")
    f=open("venue.txt","w")
    f.write("name")
    f=open("venue.txt","r")
    for line in f:
        line=line.split(",")
        print(line)
        for i in line:
            i.split()
            dic["name"]=i[0]
            dic["num"]=i[1]
            dic["cost"]=i[2]
        venuelist.append(dic)
        return(venuelist)

