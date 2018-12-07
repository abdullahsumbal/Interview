import java.io.*;
import java.util.*;


class collections{
	public static void main(String args[]){
    System.out.println("LinkedList:");
    LinkedList<Integer> queue = new LinkedList<>();
    queue.add(3);
    queue.add(4);
    queue.addFirst(5);
    queue.addLast(6);
    Iterator<Integer> it = queue.listIterator();

    while(it.hasNext()){
      System.out.print(it.next()+ " ");
    }
    System.out.println("LinkedList:");

    if(queue.contains(3)){
      System.out.println("yes it contains : " + 3);
    }

    queue.remove(1);

    //https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html



  }
}
// This code is contributed by Aakash Hasija
