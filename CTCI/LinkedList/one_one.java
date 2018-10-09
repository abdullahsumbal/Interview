/*
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
*/

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

public class one_one{

  public static void main(String[] args) {
    /* Start with the empty list. */
    LinkedList llist = new LinkedList();

    llist.head  = new Node(1);
    Node second = new Node(2);
    Node third  = new Node(2);
    llist.head.next = second;
    second.next = third;

    System.out.println(removeDup(llist.head));

    }

  public static boolean removeDup(Node head){
    HashSet <Integer> hs = new HashSet<>();
    Node prev =null;
    while (head != null) {
      System.out.println( head.data);
      // found dup
      if(hs.contains(head.data)){
          prev.next = head.next;
      }else{
        hs.add(head.data);
        prev = head;
      }

      head = head.next;
  }
   return true;
  }
}
