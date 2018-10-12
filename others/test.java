
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.*;
class test {
    public static void main(String[] args) {

        // write your code in Java SE 83, '1A 1B,2C 2C', '1B'

            String s = "1A 1B,2C 2C";
    String t = "1B";
    String [] hit = t.split(" ");
    String [] sArr = s.split(", ");
    //System.out.println(Arrays.toString(hit));
    int des = 0;
    int notDes = 0;
    for (int i =0; i < sArr.length; i++){
      HashSet <String> hs = new HashSet<>();
      System.out.println(sArr[i]);
      hs = splitString(sArr[i]);

      for(int j =0; j< hit.length; j++){
        //System.out.println(hit[j]);
        hs.remove(hit[j]);
      }
    System.out.println("-----ship aftwr------");
    Iterator<String> y = hs.iterator();
    while (y.hasNext())
      System.out.println(y.next());

     System.out.println("---------------");

      if(hs.size() == 0){
        des++;
      }else{
        notDes++;
      }
    }
    System.out.print(des);
    System.out.print(notDes);
    }

      public static  HashSet <String> splitString(String ship){
    char r1 = ship.charAt(0);
    char r2 = ship.charAt(3);
    char c1 = ship.charAt(1);
    char c2 = ship.charAt(4);
    HashSet <String> hs = new HashSet<>();

    if(r1 == r2){
        char start = c1;
        while(start <= c2){
          hs.add(String.valueOf(r1) +String.valueOf(start));
          start++;
        }
    }else if(c2 == c1){
      char start = r1;
      while(start <= r2){
        hs.add(String.valueOf(c1) +String.valueOf(start));
        start++;
      }
    }else{
      hs.add(String.valueOf(r1) +String.valueOf(c1));
      hs.add(String.valueOf(r1) +String.valueOf(c2));
      hs.add(String.valueOf(r2) +String.valueOf(c1));
      hs.add(String.valueOf(r2) +String.valueOf(c2));
    }

    System.out.println("-----ship positions------");
    Iterator<String> i = hs.iterator();
    while (i.hasNext())
      System.out.println(i.next());


    System.out.println("-----------");
    return hs;
  }
}
