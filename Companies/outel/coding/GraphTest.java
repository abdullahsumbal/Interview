import java.util.*;

class Node{
  int val;
  Node(int val){
    this.val = val;
  }
}

class graph{

  private int V; // No. of vertices

	// Array of lists for Adjacency List Representation
	private LinkedList<Integer> adj[];

	// Constructor
	graph(int v)
	{
		V = v;
		adj = new LinkedList[v];
		for (int i=0; i<v; ++i)
			adj[i] = new LinkedList();
	}

	//Function to add an edge into the graph
	void addEdge(int v, int w)
	{
		adj[v].add(w); // Add w to v's list.
	}

  void DFSUtil(int v, boolean [] visited){

    visited[v] = true;
    System.out.println(v);
    Iterator<Integer> it = adj[v].listIterator();

    while(it.hasNext()){
      int node = it.next();
      if(visited[node] == false){
        DFSUtil(node, visited);
      }
    }
  }

  void DFS(int v){
    // visited array
    boolean [] visited = new boolean[adj.length];


    DFSUtil(v, visited);
  }

  void BFS(int v){
    boolean [] visited = new boolean [adj.length];
    LinkedList<Integer> queue = new LinkedList<>();
    visited[v] = true;
    queue.add(v);

    while(!queue.isEmpty()){
      int node = queue.remove();
      System.out.println(node);

      Iterator<Integer> it =  adj[node].listIterator();
      while(it.hasNext()){
        int neigbour = it.next();
        if(!visited[neigbour] ){
          visited[neigbour]= true;
          queue.add(neigbour);
        }
      }
    }
  }

  void DFS1(int v){
    boolean [] visited = new boolean [adj.length];
    LinkedList<Integer> stack = new LinkedList<>();
    visited[v] = true;
    stack.add(v);

    while(!stack.isEmpty()){
      int node = stack.removeLast();
      System.out.println(node);

      Iterator<Integer> it =  adj[node].listIterator();
      while(it.hasNext()){
        int neigbour = it.next();
        if(!visited[neigbour] ){
          visited[neigbour]= true;
          stack.add(neigbour);
        }
      }
    }
  }

}


public class GraphTest{
  public static void main(String[] args) {
    graph g = new graph(4);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    g.DFS1(0);
    System.out.println("BFS");
    g.BFS(0);
  }
}
