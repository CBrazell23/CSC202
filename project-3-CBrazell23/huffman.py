class HuffmanNode:
    def __init__(self, char_ascii, freq):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq              # the frequency count associated with the node
        self.left = None              # Huffman tree (node) to the left
        self.right = None             # Huffman tree (node) to the right

    def __lt__(self, other):
        return comes_before(self, other) # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __repr__(self):
        #return {'char_ascii': self.char_ascii, 'freq': self.freq, 'left': self.left, 'right': self.right}
        return "CharASCII:{}, freq:{}, left:{}, right:{}".format(self.char_ascii,self.freq,self.left,self.right)

#Function determining whether or not a node comes before another node
#node, node --> bool
def comes_before(a, b):
    """Returns True if node a comes before node b, False otherwise"""
    if(a.freq < b.freq):
        return True
    elif(a.freq > b.freq):
        return False
    if(a.char_ascii < b.char_ascii): #If frequencies are same, breaks ties with char ascii
        return True
    return False

#Function combining two nodes
#node, node --> node
def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    #newNode = HuffmanNode(a.char_ascii, a.freq + b.freq)
    newNode = HuffmanNode(0,0)
    newNode.freq = a.freq + b.freq #Frequency is sum of two child nodes' freqs
    if (comes_before(a, b)):
        newNode.left = a
        newNode.right = b
    else:
        newNode.left = b
        newNode.right = a
    if (a.char_ascii < b.char_ascii):
        newNode.char_ascii = a.char_ascii
    else:
        newNode.char_ascii = b.char_ascii
    return newNode

#Function finding the frequency of occurences of all the characters within the file
#filename --> list
def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    list1 = [0] * 256
    inputFile = open(filename, 'r')
    txt = inputFile.read()
    for x in txt:
        list1[ord(x)] += 1 # Increments number of characters at spot pertaining to char
    inputFile.close()
    return list1

#Function that creates a huff tree using a frequency list
#list --> root node
def create_huff_tree(freq_list):
    #Input is the list of frequencies (provided by cnt_freq()).
    #    Create a Huffman tree for characters with non-zero frequency
    #    Returns the root node of the Huffman tree. Returns None if all counts are zero.
    nodes = []
    numNone = 0
    for x in freq_list:
        if (x != 0):
            numNone += 1
    if (numNone == 0 or numNone == 1): # Checks if there's zero or one none 0 integers
        return None
    for i in range(len(freq_list)):
        nodes.append(HuffmanNode(i, freq_list[i]))
    nodes.sort()
    fin = []
    for x in nodes:
        if (x.freq != 0):
            fin.append(x) #Creates list with only non zero values
    while(len(fin) > 1):
        a = fin.pop(0)
        b = fin.pop(0)
        newNode = combine(a, b)
        fin.append(newNode)
        fin.sort()
    return fin[0]

#Function that creates the code of the characters given root node
#node --> list
def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    list = [""] * 256
    return createCodeHelper(node, "", list)

#Helper function to create the code of characters given root node
#node, str, str --> list
def createCodeHelper(node, codepath, list):
    if(node.left is None or node.right is None):
        list[node.char_ascii] = codepath
    else:
        createCodeHelper(node.left, codepath + "0", list)
        createCodeHelper(node.right, codepath + "1", list)
    return list

#Function that creates the header of the file
#list --> str
def create_header(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    empty = True
    noZero = ""
    for i in range(len(freq_list)):
        if(freq_list[i] != 0):
            noZero += str(i)
            noZero += " "
            noZero += str(freq_list[i])
            noZero += " "
    noZero = noZero.strip() # Removes spaces at start and end
    return noZero

#Function that writes encoded text to output file
#file, file -->
def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    output = open(out_file, 'w')
    output.write(create_header(cnt_freq(in_file)))
    output.write("\n")

    if(create_huff_tree(cnt_freq(in_file)) == None):
        output.close()
    else:
        file = open(in_file)
        for x in file.read():
            output.write(create_code(create_huff_tree(cnt_freq(in_file)))[ord(x)])
    output.close()
    file.close()

#Function that decodes huffman encoded function
#file, file -->
def huffman_decode(encoded_file,decode_file):
    try:
        infile = open(encoded_file)
    except(FileNotFoundError):
        print("Please input valid file")
        return "Invalid Input" #In case of invalid input to skip rest of file
    prev = infile.tell()
    infile.seek(prev)
    traverse = create_huff_tree(parse_header(infile.readline()))
    code = infile.readline()
    output = open(decode_file, 'w')

    for x in code:
        if (x == "0"):
            traverse = traverse.left
        elif (x == "1"):
            traverse = traverse.right
        if (traverse.right == None and traverse.left == None):
            output.write(chr(traverse.char_ascii))
            infile.seek(prev)
            traverse = create_huff_tree(parse_header(infile.readline()))

    output.close()
    infile.close()

#Function that reads the header and creates the frequency list
#str --> list
def parse_header(header_string):
    list = header_string.split()
    list1 = [0] * 256
    for i in range(0, len(list), 2):
        list1[int(list[i])] = int(list[i + 1])
    return list1

#Used for quick testing purposes
def main():
    parse_header("10 2 32 8 46 1 84 1 97 3 101 5 102 2 104 2 105 7 108 5 109 2 110 4 111 1 112 3 115 3 116 3 117 2 119 1 120 1")
    huffman_decode("file1_soln.txt", "out.txt")
    #print(create_huff_tree(cnt_freq("file1.txt")))

if __name__ == "__main__":
    main()