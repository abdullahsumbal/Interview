### What is OOP?
Object-oriented programming (OOP) is a software programming model constructed around objects. This model puts data into objects (data fields) and describes object contents and behavior through the declaration of classes (methods).

### Advantages of OOP?
Modifiability: It is easy to make minor changes in the data representation
Extensibility: Adding new features
Reusability: Objects can be reused in different programs.

### What is the diamond problem in inheritance?
In case of multiple inheritance, suppose class A has two subclasses B and C, and a class D has two super classes B and C.If a method present in A is overridden by both B and C but not by D then from which class D will inherit that method B or C? This problem is known as diamond problem.

### Why Java does not support multiple inheritance?
Java was designed to be a simple language and multiple inheritance introduces complexities like diamond problem. Inheriting states or behaviors from two different type of classes is a case which in reality very rare and it can be achieved easily through an object association.

### What is method hiding in Java?
 When you declare two static methods with same name and signature in both superclass and subclass then they hide each other i.e. a call to the method in the subclass will call the static method declared in that class and a call to the same method is superclass is resolved to the static method declared in the super class.


### Can we prevent overriding a method without using the final modifier? (answer)
Yes, you can prevent the method overriding in Java without using the final modifier. In fact, there are several ways to accomplish it e.g. you can mark the method private or static, those cannot be overridden.

### Can we have a non-abstract method inside interface? (answer)
From Java 8 onward you can have a non-abstract method inside interface, prior to that it was not allowed as all method was implicitly public abstract. From JDK 8, you can add static and default method inside an interface.

### What is composition in java?
This is the has a relationship in java. Benefit of using composition in java is that we can control the visibility of other object to client classes and reuse only what we need.
https://www.journaldev.com/1325/composition-in-java-example
