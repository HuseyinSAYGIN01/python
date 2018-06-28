def asalmı(x):
    if (x==1):
        return False
    elif (x==2):
        return True
    else:
        i=2
        while (i<x):
            if (x%i==0):
                return False
            i +=1
    return True
print(list(filter(asalmı,range(0,100))))