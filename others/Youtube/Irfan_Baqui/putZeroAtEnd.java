import java.util.*;

class putZeroAtEnd{

public static void main(String[] args) {
  int [] arr =  {1,0,3,0,4,0,0,0,0,0,0,0,8};


  int arrLen = arr.length;
  int leftIndex = findZero(0, arr);
  int rightIndex = findNonZero(arrLen -1, arr);


  while(leftIndex < rightIndex){
    arr = swap(leftIndex, rightIndex, arr);
    //find zero from left
    leftIndex = findZero(0, arr);


    // find non-zero from rightIndex
    rightIndex = findNonZero(arrLen -1, arr);

  }

  System.out.println(Arrays.toString(arr));



}

static int [] swap(int leftIndex, int rightIndex, int [] arr){
  int temp = arr[rightIndex];
  arr[rightIndex] = arr[leftIndex];
  arr[leftIndex]  = temp;
  return arr;
}

static int findZero(int leftIndex, int [] arr){
  while(arr[leftIndex] != 0){
    leftIndex++;
  }
  return leftIndex;
}
static int findNonZero(int rightIndex, int [] arr){
  while(arr[rightIndex] == 0){
    rightIndex--;
  }
  return rightIndex;
}

}
