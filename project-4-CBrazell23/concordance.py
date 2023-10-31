import sys

from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    #Function that creates a stop table using the stop words txt
    #str -->
    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        infile = open(filename)
        stopList = infile.readlines()
        self.stop_table = HashTable(191)
        for x in stopList:
            x = x.strip("\n") #Removing end of line
            self.stop_table.insert(x, 0)
        infile.close()

    #Function that creates a concordance table using a given file name
    # str -->
    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError"""
        infile = open(filename)
        self.concordance_table = HashTable(191)
        numLines = 0
        for x in infile:
            numLines += 1
        infile.close()
        infile = open(filename)
        list2 = []
        baddies = string.punctuation
        baddies += "1234567890" #All the punctuation and things to remove
        for i in range(numLines):
            x = infile.readline()
            x = x.strip("\n")
            x = x.lower()

            for j in "-":
                x = x.replace(j, " ")
            for j in baddies:
                x = x.replace(j, '') # Removing all the unwanted characters
            list2.append((x, i + 1))
        for x in list2:
            list3 = x[0].split()
            for word in list3:
                if(not self.stop_table.in_table(word)):
                    self.concordance_table.insert(word, [x[1]])
        for i in range(sys.maxsize):
            try:
                if(self.concordance_table.hash_table[i] is None):
                    pass
            except(IndexError):
                break
            if (self.concordance_table.hash_table[i] is None):
                pass
            else:
                list25 = []
                for x in self.concordance_table.hash_table[i][1]:
                    if(isinstance(x, list)):
                        list25.append(x[0])
                    else:
                        list25.append(x)
                self.concordance_table.hash_table[i] = (self.concordance_table.hash_table[i][0], list25)
        for x in self.concordance_table.hash_table:
            if(x == None):
                pass
            else:
                x = (x[0], x[1].sort())

    # Function that writes the concordance onto an output file
    # str -->
    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        outfile = open(filename, 'w')
        list1 = self.concordance_table.get_all_keys()
        list1.sort()
        for x in list1:
            str1 = str(self.concordance_table.hash_table[self.concordance_table.get_index(x)][1])
            for i in ",[]":
                str1 = str1.replace(i, '')
            outfile.write(x + ": " + str1 + '\n')