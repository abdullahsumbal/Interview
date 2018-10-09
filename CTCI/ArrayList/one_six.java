import java.util.*;

public class one_six{

  public static void main(String[] args) {
    String s = "aaabbbccdd";
    int sLen = s.length();
    StringBuilder sb = new StringBuilder();
    int count = 0;
    if(sLen == 0){
      System.out.println("No String");
    }
    for(int i = 0; i < sLen ; i++){
      count++;
      if(i + 1 >= s.length() || s.charAt(i) != s.charAt(i + 1)){
        sb.append(s.charAt(i));
        sb.append(count);
        count = 0;
      }
    }
    System.out.println(sb.toString());
  }


}
