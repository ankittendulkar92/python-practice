# sum of prime factors or copy paste problem 

def prime_factor_sum(n):
    summ=0
    p=2
    while p**2<=n:
        while n%p==0:
            summ=summ+p
            n//=p
        p=p+1
    if n>1:
        summ+=n
    return summ
