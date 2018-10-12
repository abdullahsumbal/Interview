import java.util.*;

class k_most{
  public static void main(String[] args) {
    int [] inputs = {1,2,3,4,4,3,1,4};
    HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
    for(int index = 0; index < inputs.length; index++){
      // If the key is already in the HashMap
      // then increment value
      int input = inputs[index];
      if(hm.containsKey(input)){
        hm.put(input, hm.get(input) + 1);
      }else{
        hm.put(input, 1);
      }
    }
    for(HashMap.Entry<Integer, Integer> entry: hm.entrySet()){
      System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
    }
  }
}
