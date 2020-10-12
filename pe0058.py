from pe0003 import isprime

if __name__ == "__main__":
    spiral_side_length = 1
    num_diagonal_primes = 0
    num_diagonals = 1
    prime_ratio = 1.0  # So as not to immidiately exit the loop
    current_num = 1
    while prime_ratio > 0.1:
        num_diagonals += 4
        spiral_side_length += 2
        increment_this_spiral = spiral_side_length - 1
        # Now look at all four corners
        for i in range(4):
            current_num += increment_this_spiral
            if isprime(current_num):
                num_diagonal_primes += 1
        # Re-calculate the prime ratio
        prime_ratio = float(num_diagonal_primes)/float(num_diagonals)
    print(spiral_side_length)
