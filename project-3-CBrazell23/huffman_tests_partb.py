import unittest
from huffman import *

class TestList(unittest.TestCase):

   def testParse1(self):
       infile = open("file1_out.txt")
       list = infile.readline()
       code = infile.readline()
       self.assertEqual(list[:-1], "32 3 97 4 98 3 99 2 100 1")
       self.assertEqual(code, "11011011000011011010011010011")
       infile.close()

   def testParse2(self):
       infile = open("file2_out.txt")
       list = infile.readline()
       code = infile.readline()
       self.assertEqual(list[:-1], "97 2 98 4 99 8 100 16 102 2")
       self.assertEqual(code, "111111111111111101010101010101010010010010010000000000010001")
       infile.close()

   def testParse3(self):
       infile = open("multiline_out.txt")
       list = infile.readline()
       code = infile.readline()
       self.assertEqual(list[:-1], "10 2 32 8 46 1 84 1 97 3 101 5 102 2 104 2 105 7 108 5 109 2 110 4 111 1 112 3 115 3 116 3 117 2 119 1 120 1")
       self.assertEqual(code, "0111011100010001011011000101101001111011011111001000011110010100000111100101111000011111010011110110110011010100111010110101011111000001111001011110011000110110001011100111101000011010001000001111101000100110111110101011100")
       infile.close()

   def testParse4(self):
       infile = open("empty.txt")
       list = infile.readline()
       code = infile.readline()
       self.assertEqual(list[:-1], "")
       self.assertEqual(code, "")
       infile.close()

   def testParse5(self):
       infile = open("onechar.txt")
       list = infile.readline()
       code = infile.readline()
       self.assertEqual(list[:-1], "")
       self.assertEqual(code, "")
       infile.close()

   def testDecode1(self):
        huffman_decode("file1_soln.txt", "out.txt")
        self.assertTrue(compare_files("file1.txt", "out.txt"))

   def testDecode2(self):
        huffman_encode("declaration.txt", "outdec.txt")
        huffman_decode("outdec.txt", "fixed.txt")
        self.assertTrue(compare_files("declaration.txt", "fixed.txt"))

   def testDecode3(self):
       self.assertEqual(huffman_decode("FALSEFILE.txt", "nope.txt"), "Invalid Input")

   def test_parse_header(self):
      header = "97 2 98 4 99 8 100 16 102 2"
      freqlist = parse_header(header)
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_decode_01(self):
      huffman_decode("file1_soln.txt", "file1_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      self.assertTrue(compare_files("file1.txt", "file1_decode.txt"))

   def test_decode_02(self):
      huffman_decode("declaration_soln.txt", "declaration_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      self.assertTrue(compare_files("declaration.txt", "declaration_decode.txt"))

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