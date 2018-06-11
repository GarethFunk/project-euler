from fractions import Fraction

def nthtermroot2approx(n):
    if n == 1:
        return 1 + Fraction(1, 2)
    else:
        ans = Fraction(1, 2)
        for i in range(1, n):
            ans = 1/(2 + ans)
        return 1 + ans

if __name__ == "__main__":
    num_more_dig_in_numerator = 0
    for i in range(1, 1001):
        # Inefficient to keep calling this function because all terms are re-calculated
        # An iterator would be better for this case. 
        term = nthtermroot2approx(i)
        if len(str(term.numerator)) > len(str(term.denominator)):
            num_more_dig_in_numerator += 1
    print(num_more_dig_in_numerator)

