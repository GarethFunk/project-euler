import numpy as np
import matplotlib.pyplot as plt

def decode(encoded, key=None):
    if key is None:
        return [str(unichr(int(x))) for x in encoded]
    else:
        return [char^key.next() for char in encoded]


class password:
    def __init__(self, pwd):
        self.i = 0
        self.length = len(pwd)
        if type(pwd) is list:
            if type(pwd[0]) is not int:
                self.pwd = [ord(x) for x in pwd]
            else:
                self.pwd = pwd
        else:
            raise ValueError()

    def __iter__(self):
        return self

    def next(self):
        ret = self.pwd[self.i%self.length]
        self.i += 1
        return ret
    
    def reset(self):
        self.i = 0
    
    def __str__(self):
        return "".join([str(unichr(char)) for char in self.pwd])

if __name__ == "__main__":
    with open("pe0059_cipher.txt") as f:
        raw_cipher = f.read()
    # Convert to a list
    cipher = raw_cipher.split(",")
    cipher = [int(x) for x in cipher]
    print(len(cipher))
    #print(cipher)
    # let's plot a character histogram and see which characters are most common
    plt.hist(cipher, bins=list(range(max(cipher))))
    plt.show()
    # most common is 80 (107/1455)
    # Given that the password is three characters long, the single most common character
    # in the source would be the three most common characters in the output
    # There are 26^3 possible passwords (17,576)
    # Let's find passwords where the most common output char is space (ascii 32) (615 in total)
    good_pwds = []
    for a in range(26):
        # ascii lowercase starts at 97 (a) and ends at 122 (z)
        a += 97
        print(str(unichr(a)))
        for b in range(26):
            b += 97
            for c in range(26):
                c += 97
                pwd = password([a, b, c])
                decoded = decode(cipher, pwd)
                count, bins = np.histogram(decoded, bins=list(range(max(decoded))))
                del decoded
                most_common_char = bins[np.argmax(count)]
                if most_common_char == 32:
                        pwd.reset()
                        good_pwds.append(pwd)
                else:
                    del pwd
    print(len(good_pwds)) # length is 615 (down from 17,576)
    
    # Let's run through them
    for pwd in good_pwds:
        #print(str(pwd))
        #print("".join(decode(decode(cipher, pwd))))
        #raw_input()
        pass

    # Having found the password we can now calulate the sum
    pwd = password(["e", "x", "p"])
    print("".join(decode(decode(cipher, pwd))))
    pwd.reset()
    print(sum(decode(cipher, pwd)))