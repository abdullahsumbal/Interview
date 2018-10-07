import java.util.*;


class one_three{

  public static void main(String[] args) {
    String url = "Mr John Smith";
    int urlLength = 13;
    System.out.println(URLify(url, 13));
  }

  public static String URLify(String url, int len){
    StringBuilder newURL = new StringBuilder();
    int index = 0;
    while(index != len){
      if(url.charAt(index)== ' '){
        newURL.append("%20");
      }else{
        newURL.append(url.charAt(index));
      }
      index++;
    }
    return newURL.toString();
  }
}
