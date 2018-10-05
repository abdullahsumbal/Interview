class Node{
    int value;
    Node left;
    Node right;

    Node(int value) {
        this.value = value;
        right = null;
        left = null;
    }
}

class BinaryTree{
  Node root;

  public BinaryTree(){
    root = null;
  }

  public BinaryTree(int value){
    root = new Node(value);
  }

  public void add(int value) {
    root = addRecursive(root, value);
}

  public Node addRecursive(Node node, int value){
      if (node == null){
        return new Node(value);
      }
      if(node.value < value){
          node.right = addRecursive(node.right, value);
      }else if(node.value > value){
        node.left = addRecursive(node.left, value);
      }else{
        return node;
      }
      return node;
  }
}

public class Implementation{
    public static void main(String [] args){
      BinaryTree bt = new BinaryTree();
      bt.add(6);
      bt.add(4);
      bt.add(8);
      bt.add(3);
      bt.add(5);
      bt.add(7);
      bt.add(9);
      NodeA j = new NodeA(1);

      System.out.println(bt.root.left.right.value);
    }

}
