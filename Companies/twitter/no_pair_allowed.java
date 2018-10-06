

class no_pair_allowed {

  public static void main(String[] args) {

    int length = 3;
    String [] words = {"abccccc","book","yoloo"};

    for(String word : words){
      int wordLength = word.length();
      int dupCounter = 1;
      int removeDupCounter = 0;
      char previousChar;
      if(wordLength > 0){
        previousChar = word.charAt(0);
      }else{
        continue;
      }
      for (int charIndex = 1; charIndex < wordLength; charIndex++){
        char currentChar = word.charAt(charIndex);
        if(currentChar == previousChar){
          // there is a dup
          dupCounter++;
        }else{
          // there is no dup
          if(dupCounter > 1){
            removeDupCounter += dupCounter/2;
          }
          dupCounter = 1;
        }
        previousChar = currentChar;
      }// End Inner for loop
      // Edge Case: last two elements are the same
      if(dupCounter > 1){
        removeDupCounter += dupCounter/2;
      }
      System.out.println("word : "+ word + "| Remove : " + Integer.toString(removeDupCounter));
    }// End Outer for loop
  }
}
