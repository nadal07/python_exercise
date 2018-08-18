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
answer = 1
mod_value = (1000000000 + 7)
print (mod_value)
#print (1000000000)
for i in range(0,size):
    answer = (answer * b[i]) % mod_value
print (answer)
