from EMath import *
class Fraction() :
    
    def __init__ (self,*args) :
        try:
            whole = 0
            if len(args) == 2:
                if not isinstance(args[0], int) or not isinstance(args[1], int):                   
                    raise ValueError
                self.numerator = args[0]
                self.denominator = args[1]
            elif len(args) == 1:
                ar = args[0].split()
                if len(ar) == 2:
                    whole = int(ar[0])
                    ar.pop(0)
                ar = ar[0].split('/')
                self.denominator = int(ar[1])
                self.numerator = int(ar[0]) + whole * self.denominator
            if self.denominator == 0:
                raise ValueError
            self.simplify()
        except:
            self.numerator = 0
            self.denominator = 1
            print("Invalid input")
            
    def __str__(self):
        if self.numerator == 0:
            return "0"
        elif abs(self.numerator) > self.denominator:
            w = self.numerator // self.denominator
            n = abs(self.numerator) % self.denominator
            if n != 0:
                return f"{w} {n}/{self.denominator}"
            else:
                return f"{w}"
        else:
            return f"{self.numerator}/{self.denominator}"
        
    def add(self,fr:"Fraction") -> "Fraction":
        #adds fractions
        #finds lcn
        lcn = leastCommonMuliply(self.denominator, fr.denominator)
        #converts denominator to lcn and multiplys it to numerator
        temp = lcn // self.denominator * self.numerator
        #does the same thing as above
        temp2 = lcn // fr.denominator * fr.numerator
        # makes a new fraction with the new numerator and denominator
        newFraction = Fraction(temp+temp2, lcn)
        # siplify + return
        newFraction.simplify()
        return newFraction

    def subtract (self,fr:"Fraction") -> "Fraction":
        #subtracts fractions
        #finds lcn
        lcn = leastCommonMuliply(self.denominator,fr.denominator)
        #converts denominator to lcn and multiplys it to numerator
        temp = lcn // self.denominator * self.numerator
        #does the same thing as above
        temp2 = lcn // fr.denominator * fr.numerator
        # makes a new fraction with the new numerator and denominator
        newFraction = Fraction(temp-temp2, lcn)
        #print(newFraction)
        # siplify + return
        newFraction.simplify()
        return newFraction

    # multiply method
    def multiply (self,fr:"Fraction") -> "Fraction" :
        return Fraction(self.numerator * fr.numerator,self.denominator * fr.denominator)

    # divide method
    def divide (self,fr:"Fraction") -> "Fraction" :
        # flips the second number over
        temp = Fraction(fr.denominator,fr.numerator)
        # multiplys the first with the second fraction
        return self.multiply(temp)

    # simplify self
    def simplify (self) -> None :
        # set the great common factor = 1
        GCF = 1 
        # get a list of common factor for both numerator and denominator

        nFactor = factorize(self.numerator)
        dFactor = factorize(self.denominator)
        # look for the great common factor in the list
        x = len(nFactor)-1
        for i in range(x,0,-1):
            if nFactor[i] in dFactor:
                GCF = nFactor[i]
                break
        # set new denominator and numerator
        self.denominator //= GCF
        self.numerator //= GCF
        return self

    # compares two fractions and see if they are equal
    # return True if they are equal,otherwise return False
    def isEqual(self,fr) :
        self.simplify()
        fr.simplify()
        #print(self.subtract(fr).simplify())
        if self.subtract(fr).numerator == 0:
            return True
        return False
        
    def __add__(self,fr):
        return self.add(fr)
    
    def __sub__(self, fr):
        return self.subtract(fr)

    def __mul__(self, fr):
        return self.multiply(fr)

    def __truediv__(self, fr):
        return self.divide(fr)

    def __lt__(self, other):
        result = self.subtract(other)
        return result.numerator < 0

    def __le__(self, other):
        result = self.subtract(other)
        return result.numerator <= 0

    def __eq__(self, other):
        result = self.subtract(other)
        return result.numerator == 0

    def __ne__(self, other):
        result = self.subtract(other)
        return result.numerator != 0

    def __gt__(self, other):
        result = self.subtract(other)
        return result.numerator > 0

    def __ge__(self, other):
        result = self.subtract(other)
        return result.numerator >= 0


# Testing Area
if __name__ == "__main__":
    f1 = Fraction("5/12")
    f2 = Fraction("9/10")
    #print(f1.subtract(f2))

    print(f"{f1} + {f2} : {f1 + f2}") 
    print(f"{f1} * {f2} : {f1 * f2}") 
    print(f"{f1} / {f2} : {f1 / f2}") 
    print(f"{f1} - {f2} : {f1 - f2}") 
    print(f"{f1} < {f2}  : {f1 < f2}") 
    print(f"{f1} <= {f2}  : {f1 <= f2}")
    print(f"{f1} = {f2}  : {f1 == f2}")
    print(f"{f1} != {f2}  : {f1 != f2}")
    print(f"{f1} > {f2}  : {f1 > f2}") 
    print(f"{f1} >= {f2}  : {f1 >= f2}")
    