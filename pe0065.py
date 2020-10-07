#!/usr/bin/python3

# https://en.wikipedia.org/wiki/Continued_fraction#Regular_patterns_in_continued_fractions 
# There is a pattern in the contiued fraction coefficients for e
class ContinuedFractionE:
    def __init__(self, max_terms=10):
        self.term_limit = max_terms

    def __iter__(self):
        self.terms = 0
        self.start = True
        self.period = 1
        self.sub_period = 0
        return self

    def __next__(self):
        if self.terms >= self.term_limit:
            raise StopIteration
        if self.start is True:
            self.start = False
            val = 2
        else:
            self.sub_period +=1
            if self.sub_period == 1:
                val = 1
            elif self.sub_period == 2:
                val = 2 * self.period
            elif self.sub_period == 3:
                self.sub_period = 0
                self.period += 1
                val = 1
        self.terms += 1
        return val



if __name__ == "__main__":
    from math import e, sqrt
    cf = ContinuedFractionE(100)
    # https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
    h = [0, 1]
    k = [1, 0]
    n = 2  # actually 0 but we need -1 and -2 for the startup
    for an in cf:
        hn = (an * h[n-1]) + h[n-2]
        kn = (an * k[n-1]) + k[n-2]
        h.append(hn)
        k.append(kn)
        n += 1
        print(an)
    print(h[-1], k[-1])
    print(h[-1]/k[-1] - e)
    print(sum([int(x) for x in str(h[-1])]))
