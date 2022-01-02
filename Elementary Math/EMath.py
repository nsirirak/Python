def isOdd(num:int)->(bool):
    """
    function return True if the given is odd otherwise return False
    :param: int
    :return: Boolean
    """
    if num % 2 == 1: return True
    return False

def isPrime(num:int)->(bool):
    """
    function return whether the given is prime number or not
    :param: int
    :return: Boolean
    """
    if num < 1: return False
    if num % 2 == 0: return False
    limit = int(num ** 0.5) + 1
    for n in range(3, limit, 2):
        if num % n == 0: return False
    return True

def factorize(num:int) ->list:
    """
    return a list of factors of a given number
    param: int
    return: list of int
    """
    num = abs(num)
    root = int(num ** 0.5) + 1
    i = 1
    bound = num
    fact = []
    while i < bound and i <= root:
        if num % i == 0:
            fact.append(i)
            bound = num // i
            fact.append(bound)
        i += 1
    return sorted(set(fact))

def greatestCommonFactor(m:int, n:int) ->int:
    """
    Return a greatest common factor of a given two numbers
    param: int, int
    return: GCF
    """
    GCF = 1
    mFactor = factorize(m)
    nFactor = factorize(n)
    x = len(nFactor)-1
    for i in range(x,0,-1):
        if nFactor[i] in mFactor:
            GCF = nFactor[i]
            break
    return GCF

def leastCommonMuliply(m:int, n:int) ->int: 
    """
    Return a least common multiply of a given two numbers
    param: int, int
    return LCM
    """      
    large = max(m,n)
    small = min(m,n)
    # if large is divisible by small returns large       
    if large % small == 0: return large        
    lcm = large
    while lcm % small != 0:
            lcm += large
    return lcm

if __name__ == '__main__':
    print(f"Is 33 an odd number? {isOdd(33)}")
    print(f"Is 56 an odd number? {isOdd(56)}")
    print(f"Is 271 a prime number? {isPrime(271)}")
    print(f"Is 147 a prime number? {isPrime(147)}")
    print(f"The factors of 256 are {factorize(256)}")
    print(f"The greatest common factor of 64 and 120 is {greatestCommonFactor(64,120)}")
    print(f"the least common multiplyer of 8 and 15 is {leastCommonMuliply(8,15)}")
