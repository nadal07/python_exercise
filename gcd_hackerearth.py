def find_gcd(a,b):
    while(b):
        a, b = b, a % b         
    return a

size = int(input())
mul = 1
a = [0 for x in range(size)]  
for i in range (0,size):
    a[i] = int(input())
    mul = mul * a[i]

gcd = find_gcd(a[0],a[1])
print (gcd)
for i in range(2,size):
    gcd = find_gcd(gcd,a[i])
    
print (int(mul ** gcd))
