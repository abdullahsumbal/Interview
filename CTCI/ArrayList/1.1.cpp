// Is Unique: Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures? 

#include <set>
#include <iostream>

using namespace std;
int main() {

  string testString = "abcdeff";
  set <char> st;
  pair <set<char>::iterator, bool> ptr;
  int length = testString.length();

  for (int i = 0; i < length; i++){
    ptr = st.insert(testString[i]);
    if(!ptr.second){
      cout << "False" << endl;
      return 0;
    }
  }
  cout << "True" << endl;
  return 0;
}
