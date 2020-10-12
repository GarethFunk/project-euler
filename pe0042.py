from math import sqrt


def istriangle(t):
    # It's a quadratic equaltion an^2 + bn + c = 0
    # a = 0.5, b = 0.5, c = -t
    # n = -0.5 ± sqrt(0.25 + 2t)
    # n > 0 therefore only positive sqrt is valid solution
    n = -0.5 + sqrt(0.25 + (2*t))
    # n has to be an integer
    if int(n) == n:
        return int(n)
    else:
        return 0


if __name__ == "__main__":
    f = open("pe0042_words.txt")
    raw = f.read()
    f.close()
    raw = raw.replace('"', '')
    words = raw.split(",")
    triangle_words = []
    for word in words:
        word = word.upper()
        score = 0
        for letter in word:
            score += ord(letter) - 64
        triangle_num = istriangle(score)
        if triangle_num != 0:
            triangle_words.append((word, score, triangle_num))
    print(len(triangle_words))
