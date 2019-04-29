package controller;

import java.util.Scanner;

public class AVLTreeTest
{
    public static void main(String[] args)
   {            
       Scanner scan = new Scanner(System.in);
       /* Creating object of AVLTree */
       AVLTree avlt = new AVLTree(); 
       avlt.insert("come", "đến");
       avlt.insert("back", "quay lại");
       avlt.insert("dead", "cái chết");
       avlt.insert("egg", "trứng");
       avlt.insert("grade", "lớp");
       avlt.insert("hate", "ghét");
       avlt.insert("kind", "tốt");
       avlt.insert("jump", "nhảy");
       avlt.insert("meet", "gặp");
       avlt.insert("need", "cần");
       avlt.insert("quit", "thoát");
       avlt.insert("yellow", "màu vàng");
       System.out.println(avlt.search("jump"));
       
//       System.out.println("AVLTree Tree Test\n");          
//       char ch;
//       /*  Perform tree operations  */
//       do    
//       {
//           System.out.println("\nAVLTree Operations\n");
//           System.out.println("1. insert ");
//           System.out.println("2. search");
//           System.out.println("3. count nodes");
//           System.out.println("4. check empty");
//           System.out.println("5. clear tree");
//
//           int choice = scan.nextInt();            
//           switch (choice)
//           {
//           case 1 : 
//               System.out.println("Enter integer element to insert");
//               avlt.insert( scan.nextLine(), "abc");                     
//               break;                          
//           case 2 : 
//               System.out.println("Enter integer element to search");
//               System.out.println("Search result : "+ avlt.search( scan.nextLine()));
//               break;                                          
//           case 3 : 
//               System.out.println("Nodes = "+ avlt.countNodes());
//               break;     
//           case 4 : 
//               System.out.println("Empty status = "+ avlt.isEmpty());
//               break;     
//           case 5 : 
//               System.out.println("\nTree Cleared");
//               avlt.makeEmpty();
//               break;         
//           default : 
//               System.out.println("Wrong Entry \n ");
//               break;   
//           }
//           /*  Display tree  */ 
//           System.out.print("\nPost order : ");
//           avlt.postorder();
//           System.out.print("\nPre order : ");
//           avlt.preorder();
//           System.out.print("\nIn order : ");
//           avlt.inorder();
//
//           System.out.println("\nDo you want to continue (Type y or n) \n");
//           ch = scan.next().charAt(0);                        
//       } while (ch == 'Y'|| ch == 'y');               
   }
}
