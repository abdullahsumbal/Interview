# Notes

This document should be reviewed before interview

## 1. HashMap Vs HashTable

This is the most important difference between two . HashMap is non synchronized and not thread safe.On the other hand, Hashtable is thread safe and synchronized.

When to use HashMap ?  answer is if your application do not require any multi-threading task, in other words HashMap is better for non-threading applications. Hashtable should be used in multithreading applications.

### java

```
// Equivalent
HashMap map = new HashMap();
HashMap<Object, Object> map = new HashMap<Object, Object>();

// Better way is to be explicit
Map<String, Integer> map = new HashMap<String, Integer>();
map.put(_, _)

// HashSet
HashSet<String> h = new HashSet<String>();
h.add(_)

// adding and retiring is O(1)

// Iterate in java
for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
}

for (String key : hashMap.keySet()) {
    System.out.println("Key: " + key + ", Value: " + map.get(key));
}

// create an iterator
Iterator iterator = newset.iterator();

for (String temp : hset) {
   System.out.println(temp);
}
```


### Python
```
# Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
```


### C
```
No build-in
```

### C++
```
std::map<std::string, int> wordMap;

std::unordered_map<std::string, int> wordUOMap;

// Different ways of iterating maps
https://stackoverflow.com/questions/26281979/c-loop-through-map
```

## 2. ArrayList vs Vector vs LinkedList (java)

ArrayList is implemented as a resizable array. As more elements are added to ArrayList, its size is increased dynamically. It's elements can be accessed directly by using the get and set methods, since ArrayList is essentially an array.

LinkedList is implemented as a double linked list. Its performance on add and remove is better than Arraylist, but worse on get and set methods.

Vector is similar with ArrayList, but it is synchronized.

```
List<String> supplierNames1 = new ArrayList<String>();
List<String> supplierNames2 = new LinkedList<String>();
List<String> supplierNames3 = new Vector<String>();
```

## 2. Set in C++

std::set is commonly implemented as a red-black binary search tree. Insertion on this data structure has a worst-case of O(log(n)) complexity, as the tree is kept balanced.

```
#include<set> // for set operations
set<int> st;

// declaring pair for return value of set containing
// set iterator and bool
pair< set<int>::iterator,bool> ptr;

// using insert() to insert single element
// inserting 20
ptr = st.insert(20);

// checking if the element was already present or newly inserted
if (ptr.second)
    cout << "The element was newly inserted" ;
else cout  << "The element was already present";

```


## List functions

```
List <String> l = new ArrayList<>();
l.add("")
l.size()
l.remove("")
l.contains("")

```
