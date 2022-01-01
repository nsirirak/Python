# Elementary Math
This file contains Python code for fundamental math functions.
### Is the number is odd or even
This is probably your first challenge when you start coding. We simply check the remainder of the given number divided by two. The % operator given the remainder. In the case of % by 2, if the value of the expression is 0, the given number is even otherwise it is odd.
```python
def isOdd(num:int)->(bool):
    if num % 2 == 1: return True
    return False
```
---
<br>

### Is the number prime
We all know the difinition of prime number. Prime number is the number that can only divide evenly by itself and one. It means an expression ```num % n``` will be 0 only when ```num``` equal ```n``` thus we can use for loop statement to check the expression. The number is prime when the loop check never have value 0 from the statement ```num % n```. Any even number except 2 is not a prime number so we can check this before enter the loop
```python
def isPrime(num:int)->(bool):
        if num % 2 == 0: return False
        for n in range(3, num):
            if num % n == 0: return False
        return True
```
---
<br>

The function above is work but consider what happens if we give it a large odd integer. It will test every single number in a loop, which is waste of the time. We can limit the test to the root of the given number because the result of division beyond the root is smaller than the number that has been iterated. We also can skip all the even numbers since any even number except 2 are not a prime number.
```python
def isPrime(num:int)->(bool):
        """
        function return whether the given is prime number or not
        :param: int
        :return: Boolean
        """
        if num % 2 == 0: return False
        limit = int(num ** 0.5) + 1
        for n in range(3, limit, 2):
            if num % n == 0: return False
        return True

```
---
<br>

### Factorization
Factorization is the process of breaking down a large number into smaller integer numbers that, when multiplied together, return the original value.
Similar to the isPrime function, we limit the boundary checking at the root of the given number. The factorize below returns a list of a number for a given number.
```python
def factorize(num:int) ->list:
        """
        return a list of factors of a given number
        param: int
        return: list of int
        """
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
```
---
<br>

### Greatest Common Factor (GCF)
The greatest common factor is the largest number that can divide evenly into two other numbers. For example, the greatest common factor of 12 and 30 is 6. To find the GCF we use the factorize function from the previous then look for the greates common in the list.
<br>

```python
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
```
---
<br>

### Least common multiple (LCM)
Least common multiple is the smallest multiple that is exactly divisible by every member of a set of numbers. For example, the Least Common Multiple of 3 and 5 is 15 because 15 is a multiple of 3 and also a multiple of 5 and it is the smallest number like that.

<br>

```python
def leastCommonMuliply(m:int, n:int) ->int:       
        large = max(m,n)
        small = min(m,n)
        # if large is divisible by small returns large       
        if large % small == 0: return large        
        lcm = large
        while lcm % small != 0:
                lcm += large
        return lcm
```


