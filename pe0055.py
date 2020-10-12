from pe0004 import ispallindrome


def reverseadd(n):
    s = list(str(n))
    s.reverse()
    s = "".join(s)
    return n + int(s)


if __name__ == "__main__":
    num_lychrel = 9999
    for n in range(1, 10000):
        for i in range(50):
            n = reverseadd(n)
            if ispallindrome(n):
                num_lychrel -= 1
                break
    print(num_lychrel)
