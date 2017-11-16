class Fraction(object):
    def __init__(self, top, bottom):
        self.num = top
        self.denom = bottom
        if self.denom == 0:
            raise ValueError('Denominator must not be zero.')
    def __str__(self):
        return (str(self.num)) + '/' + (str(self.denom))
    def __add__(self, secondfraction):
        newnum = self.num * secondfraction.denom + self.denom * secondfraction.num
        newdenom = self.denom * secondfraction.denom
        return Fraction(newnum, newdenom)
    def __sub__(self, secondfraction):
        newnum = self.num * secondfraction.denom - self.denom * secondfraction.num
        newdenom = self.denom * secondfraction.denom
        return Fraction(newnum, newdenom)
    def __mul__(self, secondfraction):
        newnum = self.num * secondfraction.num
        newdenom = self.denom * secondfraction.denom
        return Fraction(newnum, newdenom)
    def __truediv__(self, secondfraction):
        newnum = self.num * secondfraction.denom
        newdenom = self.denom * secondfraction.num
        return Fraction(newnum, newdenom)
    def __invert__(fraction):
        return Fraction(fraction.denom, fraction.num)

fraction_one = Fraction(2,4)
fraction_two = Fraction(4,8)
fraction_add = fraction_one + fraction_two
fraction_sub = fraction_one - fraction_two
fraction_mul = fraction_one * fraction_two
fraction_div = fraction_one / fraction_two
print('Fraction one:', fraction_one, 'Fraction two:', fraction_two)
print('Fraction one + fraction two = ', fraction_add)
print('Fraction one - fraction two = ', fraction_sub)
print('Fraction one * fraction two = ', fraction_mul)
print('Fraction one / fraction two = ', fraction_div)
print('Inversion of fraction one is: ', ~fraction_one)
