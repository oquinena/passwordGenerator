#!/usr/bin/env python3

import random
import string
try:
    import pyperclip
except Exception as e:
    print('%s' % e)

class Pass:
    def __init__(self, length, pw=None):
        self.length = length
        self.pw = pw

    def generatePass(self):
        letters = string.ascii_letters
        numbers = string.digits
        mixed = f'{letters}{numbers}'
        mixed = list(mixed)
        random.shuffle(mixed)
        self.pw = random.choices(mixed, k=self.length)
        self.pw = ''.join(self.pw)
        return self.pw


def main():
    length = int(16)
    randomPass = Pass(int(length))
    randomPass.generatePass()
    pyperclip.copy(randomPass.pw)


if __name__ == '__main__':
    main()