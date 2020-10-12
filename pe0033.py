from decimal import *


class fraction():
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
        self.cancelnumerator = 0
        self.canceldenominator = 1
        self.foolishcanceled = False

    def foolishcancel(self):
        snum = str(self.numerator)
        sden = str(self.denominator)
        for digit in snum:
            if digit in sden:
                if digit == "0":
                    # This would be a trivial cancellation so we will ignore it
                    break
                snum = snum.replace(digit, "", 1)
                sden = sden.replace(digit, "", 1)
                self.cancelnumerator = int(snum)
                self.canceldenominator = int(sden)
                if self.canceldenominator != 0:
                    self.foolishcanceled = True
                break
        if self.foolishcanceled is True:
            # Now let's check if the foolish cancel is actually correct
            decimal1 = Decimal(self.numerator)/Decimal(self.denominator)
            decimal2 = Decimal(self.cancelnumerator) / \
                Decimal(self.canceldenominator)
            if decimal1 == decimal2:
                # The foolish cancel was actually correct!
                print(str(self.numerator) + "/" + str(self.denominator) + " = " +
                      str(self.cancelnumerator) + "/" + str(self.canceldenominator))
                return True
        return False


def getfractions():
    # We want to return all two digit numerator and denominator fractions less than 1
    # i.e. numerator bigger than denominator
    # where the foolish cancel method is actually correct
    fractions = []
    for denominator in range(11, 100):
        for numerator in range(10, denominator):
            frac = fraction(numerator, denominator)
            if frac.foolishcancel() is True:
                fractions.append(frac)
    return fractions


if __name__ == "__main__":
    fractions = getfractions()
    # Now we need the product of these fractions
    # Might as well use the cancelled version
    numerator = 1
    denominator = 1
    for frac in fractions:
        numerator = numerator * frac.cancelnumerator
        denominator = denominator * frac.canceldenominator
    print(str(numerator) + "/" + str(denominator))
    # The solution is the denominator when this fraction is expressed in its lowest common terms
    # it's 8/800 which is 1/100 by inspection. No need to implement a fraction canceller for a one off
