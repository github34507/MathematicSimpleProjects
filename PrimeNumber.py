def prime_number(n:int) -> bool:
    if not isinstance(n,int):
        raise TypeError('It should be an integer!')
    
    for j in range(2,int(n**0.5)+1):
        if n%j==0 or n==1:
            return False
    return True

print(prime_number(23))