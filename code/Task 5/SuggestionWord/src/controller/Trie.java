package controller;

import java.util.ArrayList;
import java.util.List;

public class Trie {
	
	public static List<String> listWords = new ArrayList<String>();
	
	public void insert(String key, TrieNode root) {
		int level;
		int length = key.length();
		int index;

		TrieNode pCrawl = root;

		for (level = 0; level < length; level++) {
			index = charToIndex(key.charAt(level));
			if (pCrawl.children[index] == null)
				pCrawl.children[index] = new TrieNode();

			pCrawl = pCrawl.children[index];
		}

		// mark last node as leaf
		pCrawl.isEndOfWord = true;
	}
	
	private int charToIndex(char ch) {
		if(ch - 'A' < 26) {
			return ch-'A';
		}
		else {
			return ch-'a'+26;
		}
	}
	
	private char indexToChar(int index) {
		if(index < 26) {
			return (char) (index + 'A');
		}
		else {
			return (char) (index-26+'a');
		}
	}
	
	private void getWords(TrieNode pCrawl, String word) {
		if(listWords.size() >= 5)
			return;
		if(pCrawl != null && pCrawl.isEndOfWord) {
			listWords.add(word);
		}
		
		for(int index=0; index<52; index++) {
			if(pCrawl.children[index] != null) {
				getWords(pCrawl.children[index], word+indexToChar(index));
			}
		}
	}

	// Returns true if key presents in trie, else false
	public boolean search(String key, TrieNode root) {
		listWords.clear();
		int level;
		int length = key.length();
		int index;
		TrieNode pCrawl = root;

		for (level = 0; level < length; level++) {
			index = charToIndex(key.charAt(level));

			if (pCrawl.children[index] == null)
				return false;

			pCrawl = pCrawl.children[index];
		}
		
		if(pCrawl != null) {
			getWords(pCrawl, key);
		}

		return (pCrawl != null && pCrawl.isEndOfWord);
	}
}
