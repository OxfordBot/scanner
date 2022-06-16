
import socket
import sys
import random
import os

class Scanner:

    def __init__(self, range_):
        self.range = range_
        self.target = socket.gethostname()
        os.system("cls")
        for self.port in range(self.range[0], self.range[1]):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0)
            self.result = self.socket.connect_ex((self.target, self.port))
            self.result = random.randint(0, 1)
            sys.stdout.flush()
            if self.result == 0:
                sys.stdout.write(u"  \u001b[42;1m")
                sys.stdout.write(" OPEN    ")
            else:
                sys.stdout.write(u"  \u001b[41;1m")
                sys.stdout.write(" CLOSED  ")
            sys.stdout.write(u"\u001b[0m")
            sys.stdout.write("  {}".format(self.port))
            sys.stdout.write("\n")
            self.socket.close()
        input()

Scanner((1000, 4000))
