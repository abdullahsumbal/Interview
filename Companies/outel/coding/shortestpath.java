  import java.util.*;


  class Graph{

    HashSet<Node> graph;

     public Graph(){
      graph = new HashSet<Node>();
     }

     public void addNode(Node n){
       graph.add(n);
     }

     public void Dijkstra(Node n){
       List <Node> visited = new ArrayList<>();
       List <Node> unvisited = new ArrayList<>();
       n.shortest_distance_from_source = 0;

       // list of visited and unvisited nodes
       for(Node node : graph){
           unvisited.add(node);
       }

       //Loop while unvisited is not empty
       while(unvisited.size() != 0){

         int shortest_distance = Integer.MAX_VALUE;
         Node target = null;
         // find the node with the shortest dostance
         for (int i = 0; i < unvisited.size(); i++){
           if(unvisited.get(i).shortest_distance_from_source < shortest_distance){
              shortest_distance = (unvisited.get(i).shortest_distance_from_source);
            }
         }
         for (int i = 0; i < unvisited.size(); i++){

           if(unvisited.get(i).shortest_distance_from_source == shortest_distance){
            target = unvisited.get(i);

            break;
          }
         }

         // find the adj nodes (excluding visisted nodes)
         // update the distances if less than stored
         for (Map.Entry<Node, Integer> entry : target.adj.entrySet()) {
             if(unvisited.contains(entry.getKey())) {
               if(entry.getKey().shortest_distance_from_source > entry.getValue() + target.shortest_distance_from_source){
                 entry.getKey().shortest_distance_from_source = entry.getValue() + target.shortest_distance_from_source;
                 entry.getKey().previous = target;
               }
             }
         }

         unvisited.remove(target);
         visited.add(target);
       }


     }

  }

  class Node{

    String name;

    //List<Node> neighbors;
    int shortest_distance_from_source = Integer.MAX_VALUE;
    Node previous = null;

    public HashMap<Node, Integer> adj;
    public Node(String name){
      this.name = name;
      //neighbors = new ArrayList<Node>();

      adj = new HashMap<Node, Integer>();
    }

    public void addDestination(Node n, int distance){
      //neighbors.add(n);
      adj.put(n, distance);
    }


  }


  public class shortestpath{
    public static void main(String[] args) {
      Node nodeA = new Node("A");
      Node nodeB = new Node("B");
      Node nodeC = new Node("C");
      Node nodeD = new Node("D");
      Node nodeE = new Node("E");
      Node nodeF = new Node("F");

      nodeA.addDestination(nodeB, 10);
      nodeA.addDestination(nodeC, 15);

      nodeB.addDestination(nodeD, 12);
      nodeB.addDestination(nodeF, 15);

      nodeC.addDestination(nodeE, 10);

      nodeD.addDestination(nodeE, 2);
      nodeD.addDestination(nodeF, 1);

      nodeF.addDestination(nodeE, 5);

      Graph graph = new Graph();

      graph.addNode(nodeA);
      graph.addNode(nodeB);
      graph.addNode(nodeC);
      graph.addNode(nodeD);
      graph.addNode(nodeE);
      graph.addNode(nodeF);

      graph.Dijkstra(nodeA);

      for (Node n: graph.graph){

        System.out.println(n.shortest_distance_from_source);
        while(n != nodeA){
          System.out.print(n.name + "->");
          n = n.previous;
        }
        System.out.println(n.name + "->");
      }
    }
  }
