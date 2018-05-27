# The numbers which will be on the corners of the spiral can be desribed with the following pattern:
# starting at 1 in the middle, the next 4 numbers are 2 apart from each other i.e. 1 + 2, 1 + 4, 1 + 6 and 1 + 8
# The next 4 numbers are 4 apart from the last number in the spiral
# The 4 after than are 6 after the last number in the spiral


def spiraldiagonals(n):
    num_spirals = int((n-1)/2)
    diag_sum = 1
    current_num = 1
    for i in range(1, num_spirals+1):
        addition_this_spiral = i*2
        # First corner
        current_num += addition_this_spiral
        diag_sum += current_num
        # Second corner
        current_num += addition_this_spiral
        diag_sum += current_num
        # Third corner
        current_num += addition_this_spiral
        diag_sum += current_num
        # Fourth corner
        current_num += addition_this_spiral
        diag_sum += current_num
    return diag_sum


if __name__ == "__main__":
    print(spiraldiagonals(5))
    print(spiraldiagonals(1001))
