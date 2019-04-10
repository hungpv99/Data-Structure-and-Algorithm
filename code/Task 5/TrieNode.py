class TrieNode: 
      
    # Trie node class 
    def __init__(self):

        #52 letter
        self.children = [None]*52
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
      
        # Returns new trie node (initialized to NULLs) 
        return TrieNode() 
  
    def _charToIndex(self,ch): 
          
        # private helper function 
        # Converts key current character into index 
        # use only 'A' through 'z' and lower case 
        if ord(ch)-ord('A') < 26:
            return ord(ch)-ord('A')
        else:
            return ord(ch)-ord('a')+26

    def _indexToChar(self, index):
        if index < 26:
            return chr(index + ord('A'))
        else:
            return chr(index - 26 + ord('a'))
  
  
    def insert(self,key): 
          
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
  
            # if current character is not present 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True
    
    def getWord(self, pCrawl, word):
        if pCrawl != None and pCrawl.isEndOfWord:
            print(word)
        for index in range(52):
            if pCrawl.children[index]:
                #word += str(self._indexToChar(index))
                self.getWord(pCrawl.children[index], word + str(self._indexToChar(index)))


    def search(self, key): 
          
        # Search key in the trie 
        # Returns true if key presents  
        # in trie, else false 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index]
        
        if pCrawl != None and pCrawl.isEndOfWord:
            self.getWord(pCrawl, key)

  
        return pCrawl != None and pCrawl.isEndOfWord 
  
# driver function 
def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["The","a","There","anaswe","any", 
            "by","Their"] 
    output = ["Not present in trie", 
              "Present in tire"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    # Search for different keys 
    print("{} ---- {}".format("Thi",output[t.search("Thi")])) 
  
if __name__ == '__main__': 
    main() 
  