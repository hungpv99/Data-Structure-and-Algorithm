package controller;

public class AVLTree {
	private AVLNode root;

	public AVLTree() {
		root = null;
	}

	public void insert(String key, String value) {
		root = insert(key, value, root);
	}

	private int height(AVLNode t) {
		return t == null ? -1 : t.height;
	}

	private int max(int lhs, int rhs) {
		return lhs > rhs ? lhs : rhs;
	}

	private AVLNode insert(String key, String value, AVLNode t) {
		
		if (t == null)  //if tree is empty, create new Node
			t = new AVLNode(key, value);
		
		else if (key.compareTo(t.key) < 0) //if key lesser key in node t, add it on sub-left tree 
		{
			t.left = insert(key, value, t.left);
			if (height(t.left) - height(t.right) == 2)  //check balance tree
				if (key.compareTo(t.left.key) < 0)  //check case to rotate
					t = rotateWithLeftChild(t);
				else
					t = doubleWithLeftChild(t);
		}
		else if (key.compareTo(t.key) > 0) //if key more key in node t, add it on sub-right tree 
		{
			t.right = insert(key, value, t.right);
			if (height(t.right) - height(t.left) == 2)  //check balance tree
				if (key.compareTo(t.right.key) > 0)  //check case to rotate
					t = rotateWithRightChild(t);
				else
					t = doubleWithRightChild(t);
		}
	
		t.height = max(height(t.left), height(t.right)) + 1;  //increase height of tree
		
		return t;
	}

	private AVLNode rotateWithLeftChild(AVLNode k2) {
		AVLNode k1 = k2.left;
		k2.left = k1.right;
		k1.right = k2;
		k2.height = max(height(k2.left), height(k2.right)) + 1;
		k1.height = max(height(k1.left), k2.height) + 1;
		return k1;
	}

	private AVLNode rotateWithRightChild(AVLNode k1) {
		AVLNode k2 = k1.right;
		k1.right = k2.left;
		k2.left = k1;
		k1.height = max(height(k1.left), height(k1.right)) + 1;
		k2.height = max(height(k2.right), k1.height) + 1;
		return k2;
	}

	private AVLNode doubleWithLeftChild(AVLNode k3) {
		k3.left = rotateWithRightChild(k3.left);
		return rotateWithLeftChild(k3);
	}

	private AVLNode doubleWithRightChild(AVLNode k1) {
		k1.right = rotateWithLeftChild(k1.right);
		return rotateWithRightChild(k1);
	}

	public String search(String val) {
		return search(root, val);
	}

	private String search(AVLNode r, String val) {
		String found = "";
		while ((r != null) && found.equals("")) {
			String rval = r.key;
			if (val.compareTo(rval) < 0)
				r = r.left;
			else if (val.compareTo(rval) > 0)
				r = r.right;
			else {
				found = r.value;
				break;
			}
			found = search(r, val);
		}
		return found;
	}
}
