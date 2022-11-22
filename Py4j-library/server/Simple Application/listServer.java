import py4j.GatewayServer;
public class listServer {
    
  public static void main(String[] args) {
      GatewayServer server = new GatewayServer();
      server.start();
      System.err.println("Server Started");

  }
}
