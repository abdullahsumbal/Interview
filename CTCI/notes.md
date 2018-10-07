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

// HashSet
HashSet<String> h = new HashSet<String>();

// adding and retiring is O(1)
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

## 2. ArrayList vs ArrayList
