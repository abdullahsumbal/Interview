import java.util.HashMap;
import java.util.Map;
import java.util.Hashtable;

public class hashtable {
    public static void main(String[] args) {
        // Creating a HashMap
      HashMap<String, Integer> numberMapping = new HashMap<String, Integer>();
      //HashMap numberMapping = new HashMap();

        // Adding key-value pairs to a HashMap
        numberMapping.put("One", 1);
        numberMapping.put("Two", 2);
        numberMapping.put("Three", 3);

        // Add a new key-value pair only if the key does not exist in the HashMap, or is mapped to `null`
        numberMapping.putIfAbsent("Four", 4);

        System.out.println(numberMapping);

        // Creating a HashTable
        Hashtable<String, Integer> numbers = new Hashtable<String, Integer>();
      //HashMap numberMapping = new HashMap();

        // Adding key-value pairs to a HashMap
        numberMapping.put("One", 1);
        numberMapping.put("Two", 2);
        numberMapping.put("Three", 3);

        // Add a new key-value pair only if the key does not exist in the HashMap, or is mapped to `null`
        numberMapping.putIfAbsent("Four", 4);

        System.out.println(numberMapping);
    }
}
