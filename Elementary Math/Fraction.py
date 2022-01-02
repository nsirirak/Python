from EMath import *
class Fraction() :
    
    def __init__ (self,*args) :
        try:
            whole = 0
            if len(args) == 2:
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
            self.simplify()
        except:
            print("Invalid input")
            
    def __str__(self):
        whole = self.numerator // self.denominator
        n = self.numerator % self.denominator
        if whole == 0 :
            return "{}/{}".format(self.numerator,self.denominator)
        if n == 0:
            return "{}".format(whole)
        return "{} {}/{}".format(whole, n, self.denominator)
        
    def add(self,fr:"Fraction") -> "Fraction":
        #adds fractions
        #finds lcn
        lcn = leastCommonMuliply(self.denominator, fr.denominator)
        #converts denominator to lcn and multiplys it to numerator
        temp = lcn // self.denominator * self.numerator
        #does the same thing as above
        temp2 = lcn // fr.denominator * fr.numerator
        # makes a new fraction with the new numerator and denominator
        newF = Fraction(temp+temp2, lcn)
        # siplify + return
        newF.simplify()
        return newF

    def subtract (self,fr:"Fraction") -> "Fraction":
        #subtracts fractions
        #finds lcn
        lcn = leastCommonMuliply(self.denominator,fr.denominator)
        #converts denominator to lcn and multiplys it to numerator
        temp = lcn // self.denominator * self.numerator
        #does the same thing as above
        temp2 = lcn // fr.denominator * fr.numerator
        # makes a new fraction with the new numerator and denominator
        newF = Fraction(temp-temp2, lcn)
        # siplify + return
        newF.simplify()
        return newF

    # multiply method
    def multiply (self,fr:"Fraction") -> "Fraction" :
        # multiply numerator together
        temp = self.numerator * fr.numerator
        # multiply denominator togeter
        temp2 = self.denominator * fr.denominator
        # make a new fraction with the new numerator and denominator
        newF = Fraction(temp,temp2)
        # simplify it and return
        newF.simplify()
        return newF

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


# Testing Area
if __name__ == "__main__":
    f1 = Fraction("1/5")
    f2 = Fraction("3/10")
    #print(f1.subtract(f2))

    f3 = f1 + f2
    print(f3)
    print(f3 - Fraction("1/3"))
    print(f1 * f2)
    print(f1/f2)
    print(Fraction("1/3").isEqual(Fraction("3/9")))
    f4 = Fraction("3t/4")