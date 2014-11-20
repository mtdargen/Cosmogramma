# ngram.py
# by Matt Dargen
#
# Class for easily constructing random sentences from text files

import random

class NGram:
    # __init__
    #   fileName = name of text corpus to be read from
    #   n = number of words per gram (must be between 2 and 4)
    #   start = symbol in text corpus representing the beginning of a sentence
    #   end = symbol in text corpus representing the end of a line
    def __init__(self, fileName, n, start="<s>", end="<e>"):
        self.r = random.Random()
        self.start = start
        self.end = end
        try:
            #open input file
            self.file = file = open(fileName,'r')

            #construct list of grams
            grams = file.read().split()
            self.n = n
            if n == 2:
                self.grams = zip(grams,grams[1:])
            elif n == 3:
                self.grams = zip(grams,grams[1:],grams[2:])
            elif n == 4:
                self.grams = zip(grams,grams[1:],grams[2:],grams[3:])
            else:
                self.grams = []
                #n outside of acceptable range
                raise Exception
        except(IOError):
            print("Error initializing NGram: " + str(fileName) + " not found")
        except(Exception):
            print("Error initializing NGram: " + str(n) + " is outside of acceptable range (2-4)")

    # setSymbols
    # sets the start and end symbols
    #   start = symbol in text corpus that represents the beginning of a sentence
    #   end = symbol in text corpus that represents the end of a line
    def setSymbols(self, start, end):
        self.start = start
        self.end = end

    # setN
    # sets the number of words per gram
    #   n = the number of words per gram
    def setN(self, n):
        try:
            grams = file.read().split()
            self.n = n
            if n == 2:
                self.grams = zip(grams,grams[1:])
            elif n == 3:
                self.grams = zip(grams,grams[1:],grams[2:])
            elif n == 4:
                self.grams = zip(grams,grams[1:],grams[2:])
            else:
                #n outside of acceptable range
                raise Exception
        except Exception:
            print("Error changing n value: n not in acceptable range")

    # generate
    # constructs a sentence from ngrams taken from specified text file
    # returns sentence (string)
    def generate(self):
        sentence = ""
        g = self.r.choice([x for x in self.grams if x[0] == self.start])
        while g[self.n-1] != self.end:
            if self.n == 2:
                g = self.r.choice([x for x in self.grams if x[0] == g[1]])
            elif self.n == 3:
                g = self.r.choice([x for x in self.grams if x[0] == g[1] and x[1] == g[2]])
            else:
                g = self.r.choice([x for x in self.grams if x[0] == g[1] and x[1] == g[2] and x[2] == g[3]])

            if g[0] != self.start:
                sentence += g[0] + " "

        if self.n == 3:
            sentence += g[1]
        elif self.n == 4:
            sentence += g[1] + " " + g[2]
        return sentence
