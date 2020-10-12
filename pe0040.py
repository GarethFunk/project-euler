#!/usr/bin/python3

def nthdigit(n):
    counter = 0
    i = 0
    while counter < n:
        # 9 x 1 (i=0)
        # 90 x 2 (i=1)
        # 900 x 3 (i=2)
        # 9000 x 4 (i=3)
        # (9x10^i)x(i+1)
        counter += (9*(10**i))*(i+1)
        i += 1
    # Roll counter back
    i -= 1
    counter -= (9*(10**i))*(i+1)
    starting_num = 10**i
    num_digits_remaining = n - counter - 1
    i += 1
    num_numbers_remaining = num_digits_remaining//i
    extra_digits = num_digits_remaining % i
    relevant_num = starting_num + num_numbers_remaining
    digit = int(str(relevant_num)[extra_digits])
    return digit


if __name__ == "__main__":
    print(nthdigit(1)*nthdigit(10)*nthdigit(100)*nthdigit(1000)
          * nthdigit(10000)*nthdigit(100000)*nthdigit(1000000))
