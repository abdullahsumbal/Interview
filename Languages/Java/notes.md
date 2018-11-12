# The following are OOP concepts in java
## 1. Abstract class

Abstraction is a process of hiding the implementation details and showing only functionality to the user.
###### An abstract class must be declared with an abstract keyword.
###### It can have abstract and non-abstract methods.
###### It cannot be instantiated.
###### It can have constructors and static methods also.
###### It can have final methods which will force the subclass not to change the body of the method.

```
abstract class Shape{  
  abstract void draw();  
}  
//In real scenario, implementation is provided by others i.e. unknown by end user  
class Rectangle extends Shape{  
  void draw(){
    System.out.println("drawing rectangle");
  }  
}  
class Circle1 extends Shape{  
  void draw(){
    System.out.println("drawing circle");
  }  
}  
//In real scenario, method is called by programmer or user  
class TestAbstraction1{  
  public static void main(String args[]){  
    Shape s=new Circle1();//In a real scenario, object is provided through method, e.g., getShape() method  
    s.draw();  
  }  
}  
```

## 2. Interface

When a class implements an interface, you can think of the class as signing a contract, agreeing to perform the specific behaviors of the interface.
```
/* File name : Animal.java */
interface Animal {
   public void eat();
   public void travel();
}

/* File name : MammalInt.java */
public class MammalInt implements Animal {

   public void eat() {
      System.out.println("Mammal eats");
   }

   public void travel() {
      System.out.println("Mammal travels");
   }

   public int noOfLegs() {
      return 0;
   }

   public static void main(String args[]) {
      MammalInt m = new MammalInt();
      m.eat();
      m.travel();
   }
}
```

## Polymorphism

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

```
List<String> l = new ArrayList<>();
```

###overriding
```
class Dog{
    public void bark(){
        System.out.println("woof ");
    }
}
class Hound extends Dog{
    public void sniff(){
        System.out.println("sniff ");
    }

    public void bark(){
        System.out.println("bowl");
    }
}

public class OverridingTest{
    public static void main(String [] args){
        Dog dog = new Hound();
        dog.bark();
    }
}
```

overloading
```
class Dog{
    public void bark(){
        System.out.println("woof ");
    }

    //overloading method
    public void bark(int num){
    	for(int i=0; i<num; i++)
    		System.out.println("woof ");
    }
}
```

## Encapsulation

This is the practice of keeping fields within a class private, then providing access to them via public methods
