import unittest
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def testComesBefore(self):
        a = HuffmanNode(4, 12)
        b = HuffmanNode(2, 14)
        self.assertTrue(comes_before(a, b))

    def testComesBefore1(self):
        a = HuffmanNode(2, 14)
        b = HuffmanNode(4, 14)
        self.assertTrue(comes_before(a, b))

    def testCombine(self):
        a = HuffmanNode(4, 12)
        b = HuffmanNode(2, 14)
        self.assertEqual(combine(a,b).freq, 26)

    def testCombine1(self):
        a = HuffmanNode(4, 12)
        b = HuffmanNode(2, 14)
        self.assertEqual(combine(a, b).char_ascii, 2)

    def testCntFreq(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 13)

    def testCntFreq1(self):
        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 56)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char_ascii, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char_ascii, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char_ascii, 100)

    def testCreateHuffTree(self):
        self.assertEqual(create_huff_tree([]), None)

    def testCreateHuffTree1(self):
        self.assertEqual(create_huff_tree([1]), None)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def testCreateCode(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '11')

    def testCreateHeader(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file2_out.txt", "file2_soln.txt"))

    def testCreateHeader1(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("multiline_out.txt", "multiline_soln.txt"))

    def testHuffmanEncode(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertFalse(compare_files("multiline.txt", "multiline_soln.txt"))

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1_out.txt", "file1_soln.txt"))

# Compare files - takes care of CR/LF, LF issues
def compare_files(file1,file2):
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match

if __name__ == '__main__': 
   unittest.main()
