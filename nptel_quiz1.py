def g(x):
    (q,d) = (1,0)
    while q <= x:
      (q,d) = (q*10,d+1)
    return(d)
def h(m,n):
    ans = 0
    while (m >= n):
      (ans,m) = (ans+1,m-n) 
    return(ans)
def h1(n):
    f = 0
    for i in range(1,n+1):
      if n%i == 0:
        f = f + 1
    return(f%2 == 1)
print (g(31415927))
print (h(231,8))
print (h1(8))
