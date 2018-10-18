import re
import unittest

def sumNums(fileName):
    inFile = open(fileName,"r")
    lines = inFile.readlines()
    counter = 0
    for x in lines:
        find_all_numbers = x.strip()
        y = re.findall('[0-9]\d*',find_all_numbers)
        for num in y:
            counter +=int(num)
    return(counter)
    pass

def countWord(fileName, word):
    inFile = open(fileName,"r")
    lines = inFile.readlines()
    counter = 0
    for x in lines:
        find_all_words = x.strip()
        y = re.findall(r"\b[Cc]omputer\b",find_all_words)
        for word in y:
            counter += 1
    return(counter)
    pass
countWord("regex_sum_42.txt","computer")
def listURLs(fileName):
    inFile = open(fileName)
    lines = inFile.readlines()
    counter = 0
    for x in lines:
        find_all_url = x.strip()
        y = re.findall('w*-c.m',find_all_url)
        print(y)
        # for num in y:
        #     counter +=1
    # return(counter)
    pass


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
