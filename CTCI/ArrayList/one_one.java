// Is Unique: Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?

class one_one{
  public static void main(String[] args) {
    String s= "abcdeff";
    System.out.println(checkDup1(s));

  }

  public static boolean checkDup(String s){
    boolean [] assci = new boolean [128];
    if(s.length() > 128) return false;

    for(int i = 0; i < s.length(); i++){
      if(assci[s.charAt(i)]) return false;
      else assci[s.charAt(i)] = true;
    }
    return true;
  }

  /*
  Assuming there are only a-z characters.
  then we can use integer.
  integer has 4 bytes.
  meaning 4*8 = 32 bits which can easily fit 26 characters
  */
  public static boolean checkDup1(String s){
    int checker  = 0;
    for(int i = 0; i < s.length(); i++){
      int val = s.charAt(i) - 'a';
      if((checker & ( 1 << val)) > 0) return false;
      else{
        checker |= ( 1 << val);
      }
    }
    return true;
  }

}
