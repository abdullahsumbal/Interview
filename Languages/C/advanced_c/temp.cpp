#include <iostream>

using namespace std;
// const used with functions
class Dog {
   int age;
   string name;
public:
   Dog() { age = 3; name = "dummy"; }

   // const parameters
   void setAge(const int& a) { age = a; }
   void setAge(int& a) { age = a; }

   // Const return value
   const string& getName() {return name;}

   // const function
   void printDogName() const { cout << name << "const" << endl; }
   void printDogName() { cout << getName() << " non-const" << endl; }
};

int main() {
  cout<<"what ever overloads"<< flush;
   Dog d;
   d.printDogName();

   const Dog d2;
   d2.printDogName();

   const string& a = d.getName();
}
