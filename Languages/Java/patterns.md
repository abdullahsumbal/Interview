### What problem is solved by Strategy pattern in Java?
ability of a program to dynamically select a strategy during runtime.

```

//Strategy Interface
public interface CompressionStrategy {
  public void compressFiles(ArrayList<File> files);
}

public class ZipCompressionStrategy implements CompressionStrategy {
  public void compressFiles(ArrayList<File> files) {
    //using ZIP approach
  }
}

public class RarCompressionStrategy implements CompressionStrategy {
  public void compressFiles(ArrayList<File> files) {
    //using RAR approach
  }
}


public class CompressionContext {
  private CompressionStrategy strategy;
  //this can be set at runtime by the application preferences
  public void setCompressionStrategy(CompressionStrategy strategy) {
    this.strategy = strategy;
  }

  //use the strategy
  public void createArchive(ArrayList<File> files) {
    strategy.compressFiles(files);
  }
}

public class Client {
  public static void main(String[] args) {
    CompressionContext ctx = new CompressionContext();
    //we could assume context is already set by preferences
    ctx.setCompressionStrategy(new ZipCompressionStrategy());
    //get a list of files...
    ctx.createArchive(fileList);
  }
}

```

### Which OOP concept Decorator design Pattern is based upon?
Decorator pattern allows a user to add new functionality to an existing object without altering its structure.
