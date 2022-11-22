from py4j.java_gateway import JavaGateway
gateway=JavaGateway()
my_list = [3,2,1]
gateway.jvm.java.util.Collections.sort(my_list)
