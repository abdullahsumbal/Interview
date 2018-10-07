import java.util.*;
import java.lang.*;

class one_five{

  public static void main(String[] args) {
    String s1 = "palerr";
    String s2 = "palere";
    int s1Length = s1.length();
    int s2Length = s2.length();
    if(Math.abs(s1Length - s2Length) > 1){
      System.out.println("False");
    }else if(s1Length != s2Length){
      // differnent length
      oneinsert(s1, s2);
    }else{
      // Check same
      oneReplace(s1, s2);
    }
  }

  public static void oneinsert(String s1, String s2){
    String first = s1.length() < s2.length() ? s2 : s1;
    String second = s1.length() > s2.length() ? s1 : s2;
    int edit = 0;
    for (int i =0; i < first.length(); i++) {
      if(first.charAt(i) != second.charAt(i + edit)){
        edit++;
        if(edit > 1){
          System.out.println("False");
          return;
        }
      }
    }
    System.out.println("True");
  }

  public static void oneReplace(String s1, String s2){
    int edit = 0;
    for (int i =0; i < s1.length(); i++) {
      if(s1.charAt(i) != s2.charAt(i)){
        edit++;
        if(edit > 1){
          System.out.println("False");
          return;
        }
      }
    }
    System.out.println("True");
  }
}
