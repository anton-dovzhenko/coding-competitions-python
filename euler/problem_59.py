import itertools


class Solution:

    @classmethod
    def xor_decryption(cls):

        with open("resources/p059_cipher.txt", 'r') as content_file:
            content = content_file.read()
        content = [int(x) for x in content.split(',')]

        for key in itertools.product(range(ord('a'), ord('z') + 1), repeat=3):
            valid = True
            decrypted = ''
            s = 0
            for i in range(len(content)):
                d = content[i] ^ key[i % 3]
                s += d
                d = chr(d)
                if not (d.isalpha() or d.isspace() or d.isnumeric() or d in ' "\'()+,./:;[]'):
                    valid = False
                    break
                decrypted += d
            if valid:
                print(decrypted)
                return s


