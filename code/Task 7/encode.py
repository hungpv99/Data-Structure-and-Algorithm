import queue
from collections import Counter
import os

class HuffmanNode(object):
    def __init__(self, left=None, right=None, data=None, freq=0):
        self.left = left
        self.right = right
        self.data = data
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        return not(self.right and self.left)


q = queue.PriorityQueue()
f = open('test.txt', 'r')
text = f.read()
f.close()

frequencies = Counter(text)

for key in frequencies:
    q.put(HuffmanNode(data=key, freq=frequencies[key]))

while q.qsize() > 1:
    l, r = q.get(), q.get()
    q.put(HuffmanNode(left=l, right=r, freq=l.freq+r.freq))

dic = {}

def generationCode(root, code):
    if root.left:
        code.append('0')
        generationCode(root.left, code)
        code.pop()
    if root.right:
        code.append('1')
        generationCode(root.right, code)
        code.pop()

    if root.isLeaf():
        s = ''
        dic[root.data] = s.join(code)


def fill_byte(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"
    return encoded_text


def get_byte_array(padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
        print("Encoded text not padded properly")
        exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b


def compress(encoded_text):
    with open('test.bin', 'wb') as output:
        padded_encoded_text = fill_byte(encoded_text)
        b = get_byte_array(padded_encoded_text)
        output.write(bytes(b))

def writeInfo():
    with open('test_info.dat', 'w') as file:
        file.write(str(len(text))+';')
        for key in dic:
            file.write(key + ":" + dic[key] + ';')


code = []
generationCode(q.get(), code)
encoded_text = ""
for ch in text:
    encoded_text += dic[ch]

compress(encoded_text)
writeInfo()
print("encode!")