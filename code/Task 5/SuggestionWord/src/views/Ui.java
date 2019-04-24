package views;

import controller.AVLTree;
import controller.Trie;
import controller.TrieNode;

import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Ui extends JFrame {

	JLabel lblSuggest;
	JTextField txtInput;
	JLabel lblResult;
	Trie trieDic;
	TrieNode rootDic;
	AVLTree avlTree;

	public Ui(String title) {
		super(title);
		
		trieDic = new Trie();
		rootDic = new TrieNode();
		
		
		avlTree = new AVLTree();
		
		createTree();
		addcontrol();
		addEvent();
	}

	private void createTree() {
		
		FileReader fr = null;
		BufferedReader br = null;
		
		try {
			
			fr = new FileReader(new File("dictionary.txt"));
			br = new BufferedReader(fr);
			String line;
			while((line = br.readLine()) != null) {
				avlTree.insert(line.substring(0,line.indexOf(" ")).trim(), line.substring(line.indexOf(" ")).trim());
				trieDic.insert(line.substring(0,line.indexOf(" ")).trim(), rootDic);
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				br.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			try {
				fr.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	

	private void addEvent() {
		// TODO Auto-generated method stub
		txtInput.addKeyListener(new KeyListener() {
			
			@Override
			public void keyTyped(KeyEvent e) {
				// TODO Auto-generated method stub
				
			}
			
			@Override
			public void keyReleased(KeyEvent e) {
				// TODO Auto-generated method stub
				lblSuggest.setText("");
				String textSuggest = "";
				String text[] = txtInput.getText().trim().split("\\s+");
				System.out.println(text.length);
				if(!text[0].equals("")) {
					trieDic.search(text[text.length-1], rootDic);
					for(int i=0; i<trieDic.listWords.size(); i++) {
						textSuggest += trieDic.listWords.get(i) + "  ";
					}
					if(Trie.listWords.size() > 0 && text[text.length-1].equals(Trie.listWords.get(0))) {
						lblResult.setText(text[text.length-1] + " : " + avlTree.search(text[text.length-1]));
					}else {
						lblResult.setText("Not matching...");
					}

						
						lblSuggest.setText(textSuggest);
						System.out.println(textSuggest);
						System.out.println(trieDic.listWords.toString());
				}
				
			}
			
			@Override
			public void keyPressed(KeyEvent e) {
				// TODO Auto-generated method stub
				
			}
		});
	}

	private void addcontrol() {
		// TODO Auto-generated method stub
		Container con = getContentPane();

		JPanel pnMain = new JPanel();
		pnMain.setLayout(new FlowLayout());
		con.add(pnMain);

		lblSuggest = new JLabel("");
		txtInput = new JTextField(50);
		lblResult = new JLabel("");
		
		lblSuggest.setPreferredSize(txtInput.getPreferredSize());
		lblResult.setPreferredSize(txtInput.getPreferredSize());

		pnMain.add(lblSuggest);
		pnMain.add(txtInput);
		pnMain.add(lblResult);

	}

	public void showWindow() {
		this.setSize(600, 200);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		this.setVisible(true);
	}
	
	public static void main(String[] args) {
		Ui ui = new Ui("Suggest Word");
		ui.showWindow();
	}
}
