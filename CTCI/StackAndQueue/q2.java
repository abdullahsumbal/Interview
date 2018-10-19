import java.util.*;


class q2{

public static void main(String[] args) {

}


}

class Node{
  int val;
  public Node (int val){
    this.val = val;
  }

}

class SetOfStack{
  List<ArrayList<Node>> stacks = new ArrayList<>();
  int max;
  int curStack;

  public SetOfStack(int max){
    List <Node> stack = new ArrayList<>();
    this.max= max;
    curStack = 0;
  }

  public void push(int val){
    if(isFull()){
      // new stack
      ArrayList <Node> newStack = new ArrayList<>();
      newStack.add(new Node(val));
      stacks.add(newStack);
      curStack++;
    }else{

      (stacks.get(stacks.size() - 1)).add(new Node(val));
    }
  }


  public boolean isFull(){
    if((stacks.get(stacks.size() - 1)).size() == max)
      return true;
    return false;
  }

  public boolean isEmpty(){
    if((stacks.get(stacks.size() - 1)).size() == 0){
      return true;
    }
    return false;
  }

}
