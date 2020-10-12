
class Polygonal():
    def __init__(self, order, max_digits=None):
        self.order = order
        self.n = 1
        self.max_digits = max_digits

    def __iter__(self):
        return self

    def __next__(self):
        p = (self.n*(((self.order - 2)*self.n) + (4 - self.order)))/2
        self.n += 1
        if self.max_digits is not None:
            if len(str(p)) > self.max_digits:
                raise StopIteration
        return p

    def next(self):
        return self.__next__()


def Post(input_num, indices_to_exlcude, polygonal_numbers):
    post = []
    for i in range(len(polygonal_numbers)):
        if i in indices_to_exlcude:
            continue
        for num in polygonal_numbers[i]:
            if input_num[1] == num[0]:
                # num could succeed input_num
                post.append((num, i))
    return post


def ConvertNum(num):
    return str(num[0]).zfill(2) + str(num[1]).zfill(2)


def PathFinder(input_num, indices_to_exlcude, polygonal_numbers):
    # This will recurse until we have gone to each column once and linked up or we fail
    if len(indices_to_exlcude) >= len(polygonal_numbers):
        # We have been through all polys
        return ConvertNum(input_num)
    else:
        posts = Post(input_num, indices_to_exlcude, polygonal_numbers)
        if len(posts) == 0:
            return False
        else:
            for post in posts:
                ret = PathFinder(
                    post[0], indices_to_exlcude + [post[1]], polygonal_numbers)
                if ret is not False:
                    return ConvertNum(input_num) + " " + ret
        return False


if __name__ == "__main__":
    max_digits = 4
    iterators = [Polygonal(3, max_digits), Polygonal(4, max_digits), Polygonal(
        5, max_digits), Polygonal(6, max_digits), Polygonal(7, max_digits), Polygonal(8, max_digits)]
    # Get all the polygonal number up to the max digits
    polygonal_numbers = [list(poly) for poly in iterators]
    # Trim off the ones with too few digits
    polygonal_numbers = [[x for x in polys if len(
        str(x)) == max_digits] for polys in polygonal_numbers]
    print("Done generating polygonal numbers")
    # Now we've got all the four digit polygonal numbers for order 4, 5, 6, 7 & 8
    # There is exactly one number from each list that together forms the required set.
    # Twist is that set is ordered and the cyclic property breaks down otherwise.
    # The quantity of numbers we have is [96, 68, 56, 48, 43, 40].
    # There are 30 billion possible combinations each of which could be ordered in 720 (6!) different ways
    # Total of 21.7 trillion possible answers to check...
    # Note: I did try cutting this down by removing all dead-end numbers from the lists but it only reduced to 1.7 trillion. Wasn't necessary.
    polygonal_numbers = [[(int(str(x)[0:2]), int(str(x)[2:])) for x in polys]
                         for polys in polygonal_numbers]  # easier for looking at digits halves
    # Now find paths. Note that we must try all possible starting points.
    for i in range(len(polygonal_numbers)):
        for num in polygonal_numbers[i]:
            ret = PathFinder(num, [i], polygonal_numbers)
            if ret is not False:
                if ret[-2:] == ret[0:2]:
                    print(ret)
                    print(sum([int(x) for x in ret.split(" ")]))
