import java.util.*;
class LinkedList
{
    Node head;  // head of list
}

/* Linked list Node*/
class Node
{
    int data;
    Node next;

    // Constructor to create a new node
    // Next is by default initialized
    // as null
    Node(int d) {data = d;}
}

public class one_two{

  public static void main(String[] args) {
    /* Start with the empty list. */
    LinkedList llist = new LinkedList();

    llist.head  = new Node(1);
    Node second = new Node(2);
    Node third  = new Node(3);
    llist.head.next = second;
    second.next = third;

    rec(llist.head, 1);

    }

    static int rec(Node head, int k){
      if (head == null){
        return 0;
      }

      int count = rec(head.next, k) + 1;
      if(count == k){
        System.out.println(head.data);
      }
      return count;
    }
  }
