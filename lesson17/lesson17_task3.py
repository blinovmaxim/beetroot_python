
from math import gcd


class Fraction:
    def __init__(self,numer,den):# num-numerator-  Числитель  . Den- denominator -Знаменатель
      self.numer=numer
      self.den=den

    def __str__(self):
        return str(self.numer)+"/"+str(self.den)

    def __add__(self,other):
        newnumer=self.numer*other.den+self.den*other.numer
        newden=self.den*other.den
        common=gcd(newnumer,newden)#gcd- greatest common divisor - наибольший общий делитель
        return Fraction(newnumer//common,newden//common)

    def __sub__(self,other):
        newnumer=self.numer*other.den-self.den*other.numer
        newden=self.den*other.den
        common=gcd(newnumer,newden)#gcd- greatest common divisor - наибольший общий делитель
        return Fraction(newnumer//common,newden//common)
    
    def __mul__(self,other):
        newnumer=self.numer*other.numer
        newden=self.den*other.den
        common=gcd(newnumer,newden)#gcd- greatest common divisor - наибольший общий делитель
        return Fraction(newnumer//common,newden//common)

    def __truediv__(self,other):
        newnumer=self.numer*other.den
        newden=self.den*other.numer
        common=gcd(newnumer,newden)#gcd- greatest common divisor - наибольший общий делитель
        return Fraction(newnumer//common,newden//common)


    def __eq__(self, other):
        firstnumer = self.numer * other.den
        secondnumer = other.numer * self.den

        return firstnumer == secondnumer
   
if __name__=="__main__":
    x=Fraction(2,7)
    y=Fraction(4,7)
    z1=x+y
    z2=x-y
    z3=x/y
    z4=x*y
    
    FractionforEq=Fraction(3,5)
    print("Первая Дробь :",x)
    print("Вторя Дробь :",y)
    print("Сложение: ",z1)
    print("Вычитание: ",z2)
    print("Деление: ",z3)
    print("Умножение: ",z4)    
    print(f"Равенство: {x+y} равно {FractionforEq} ?",x+y==FractionforEq)