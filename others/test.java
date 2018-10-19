import java.util.*;
class test {


public static void main(String[] args) {
  List <Integer> l = new ArrayList<>();
  l.add(1);
  l.add(2);
  l.add(3);
  l.add(4);
  l.add(5);
  l.add(6);
  moveEven(l);
}

static int moveEven(List <Integer> l) {
  int lastEven = 0;
    for (int cur = 0; cur < l.size(); cur++) {
        if (l.get(cur) % 2 == 0) {
          int temp = l.get(cur);
          l.add(cur, l.get(lastEven));
          l.add(lastEven, temp);
          lastEven++;

        }
    }
    //System.out.println(Arrays.toString(l));
    System.out.println(lastEven);
    return lastEven;
}
}
