package controller;

public class AVLNode {
	AVLNode left, right;
	String key;
	String value;
	int height;
	public AVLNode() {
		super();
		this.left = null;
		this.right = null;
		this.key = "";
		this.value = "";
		this.height = 0;
	}
	public AVLNode(String key, String value) {
		super();
		this.left = null;
		this.right = null;
		this.key = key;
		this.value = value;
		this.height = 0;
	}
}
