def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def sp_sequence():
    size = int(input())
    #a = [0 for x in range(size)]
    a = input()
    b=[]
    a = a.split()
    #print (a[0])
    for x in a:
        if is_number(x):
            b.append(int(x))
    #print (b)
    b.sort()
    dif = b[1] - b[0]
    for x in range(1,size-1):
        if dif != (b[x+1] - b[x]):
            return 0
    return 1

testcase = int(input())
pr = []
for x in range(0,testcase):
    a = sp_sequence()
    if a == 1:
        pr.append ("YES")
    else:
        pr.append ("NO")
for x in range (0,testcase):
    print(pr[x])
