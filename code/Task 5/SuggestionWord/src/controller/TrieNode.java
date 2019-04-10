package controller;


public class TrieNode {
	
	// Alphabet size (# of symbols)
	static final int ALPHABET_SIZE = 52;
	
	TrieNode[] children = new TrieNode[ALPHABET_SIZE];

	// isEndOfWord is true if the node represents
	// end of a word
	boolean isEndOfWord;

	public TrieNode() {
		isEndOfWord = false;
		for (int i = 0; i < ALPHABET_SIZE; i++)
			children[i] = null;
	}
	
};
