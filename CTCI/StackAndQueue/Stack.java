import java.util.*;

public class Stack{

  public static void main(String[] args) {

    StackNode s = new StackNode();
    s.push(4);
    System.out.println(s.peekMin());
    s.push(6);
    System.out.println(s.peekMin());
    s.push(2);
    System.out.println(s.peekMin());
    s.push(1);
    System.out.println(s.peekMin());

  }

}

class Node{
  int val;
  int min;
  public Node(int val){
    this.val = val;
  }
}

class StackNode{

  List <Node> node = new ArrayList<>();
  public StackNode(){

  }


  public void push(int i){
    if(isEmpty()){
      Node n = new Node(i);
      n.min = i;
      node.add(n);
    }else if(peekMin() > i){
        Node n = new Node(i);
        n.min = i;
        node.add(n);
      }else{
        Node n = new Node(i);
        n.min = peekMin();
        node.add(n);
    }
  }

  public int pop(){
    int val = node.get(node.size() - 1).val;
    node.remove(node.size() - 1);
    return val;
  }

  public int peekMin(){
    if( isEmpty())
        return -1;
    else
      return (node.get(node.size() - 1)).min;
  }

  public boolean isEmpty(){
    if (node.size() > 0)
      return false;
    return true;
  }
}
