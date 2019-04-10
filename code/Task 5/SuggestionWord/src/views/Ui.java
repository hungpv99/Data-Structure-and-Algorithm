package views;

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
	Trie trieDic;
	TrieNode rootDic;
	Trie trieCur;
	TrieNode rootCur;

	public Ui(String title) {
		super(title);
		
		trieDic = new Trie();
		rootDic = new TrieNode();
		
		trieCur = new Trie();
		rootCur = new TrieNode();
		
		createTrieDic();
		addcontrol();
		addEvent();
	}
	
	private void createTrieDic() {
		
		FileReader fr = null;
		BufferedReader br = null;
		
		try {
			
			fr = new FileReader(new File("dict_test.txt"));
			br = new BufferedReader(fr);
			String line;
			while((line = br.readLine()) != null) {
				trieDic.insert(line.trim(), rootDic);
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
					if(e.getKeyCode() == KeyEvent.VK_SPACE) {
						trieCur.insert(text[text.length-1], rootCur);
					}
					else {
						trieCur.search(text[text.length-1], rootCur);
						
						if(trieCur.listWords.size() >= 5) {
							for(int i=0; i<5; i++) {
								textSuggest += trieCur.listWords.get(i) + "  ";
							}
							
						}
						else {
							
							for(int i=0; i<trieCur.listWords.size(); i++) {
								textSuggest += trieCur.listWords.get(i) + "  ";
							}
							
							trieDic.search(text[text.length-1], rootDic);
							
							if(trieDic.listWords.size() >= 5) {
								
								for(int i = 0; i < 5; i++) {
									textSuggest += trieDic.listWords.get(i) + "  ";
								}
							}
							else {
								for(int i=0; i<trieDic.listWords.size(); i++) {
									textSuggest += trieDic.listWords.get(i) + "  ";
								}
							}
						}
						
						lblSuggest.setText(textSuggest);
						System.out.println(textSuggest);
						System.out.println(trieCur.listWords.toString());
						System.out.println(trieDic.listWords.toString());
					}
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
		
		lblSuggest.setPreferredSize(txtInput.getPreferredSize());

		pnMain.add(lblSuggest);
		pnMain.add(txtInput);

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
