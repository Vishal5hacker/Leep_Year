while(start<=stop):
    flag = 0
    if(start%4==0):
        if(start%40==0):
            if(start%400==0):
                flag = 1
            else:
                pass
        else:
            flag = 1
    else:
        pass
    if(flag == 1):
        print(start,end=" ")
    start = start + 1