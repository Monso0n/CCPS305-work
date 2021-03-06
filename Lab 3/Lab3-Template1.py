import heapq

def getName():
	return "Kainth, Mayank"

# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False
    
    def __le__(self, other):
        if self.value <= other.value:
            return True
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False
    
    def __ge__(self, other):
        if self.value >= other.value:
            return True
        return False

class MyHuffman():
    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        print("Building huffman tree with dictionary {}".format(weights))

        self.heap = []
        
        def printHeap():# function to print contents of heap later
            for i in self.heap:
                print("{}/{}".format(i.data, i.value))


        for i in weights: #populate heap with leaf nodes
            #print(f"i{i}, weights[i]{weights[i]}")
            self.heap.append(Node(weights[i], i))

        heapq.heapify(self.heap) # sort heap

        print("done appending leaf nodes and sorting heap")
        #print out min heap
        printHeap()

        print("now merging nodes")
        while True:
            a = heapq.heappop(self.heap)
            b = heapq.heappop(self.heap) if len(self.heap) >= 1 else None
            sum = a.value + b.value if b!= None else a.value
            heapq.heappush(self.heap, Node(sum, None, a, b))

            if len(self.heap) <= 1:
                break


    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        print(f"the word that was passed is {word}")
        dict = {} #create empty dictionary


        charlist = list(word) # make a list of characters in passed word
        for i in charlist:
            dict[i] = charlist.count(i)

        print(dict) # print dictionary

        self.build(dict)

        self.codeDict = dict.copy()
        self.bitstring, self.code = "",""

        def getCode(n): #this code recursively fills codeDict with the code/key for each letter
            if n.data is not None:
             #   print(f"code for {n.data} is {self.code}")
                self.codeDict[n.data] = self.code
                return
            if n.left is not None:
                self.code += "1"
                getCode(n.left)
                self.code = self.code[:-1]

            if n.right is not None:
                self.code += "0"
                getCode(n.right)
                self.code = self.code[:-1]

        getCode(self.heap[0])
        print(f"final code dict: {self.codeDict}")

        for i in word:
            self.bitstring += self.codeDict[i]
            #print(f"{self.bitstring}")
        print(f"final bitstring {self.bitstring}")


        self.decode(self.bitstring)
        return self.bitstring


    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        word = ""
        count = 0

        print(f"decoding {bitstring}")
        pos = self.heap[0]

        for i in bitstring:  #this loop decodes the word by searching through the node

            if i == "1":
                pos = pos.right
            elif i == "0":
                pos = pos.left

            if pos.data!=None:
                print(f"pp  {pos.data}")
                word += pos.data
                pos = self.heap[0]





        print(f"The decoded word is "{word}"")
        return word

"""
dict = { #Nirvana
    "N":2,
    "I":1,
    "R":1,
    "V":1,
    "A":2
}

t = {"l": 1}

a = MyHuffman()
a.encode("Nirvana")
#a.decode("1")
#a.build(dict)
"""