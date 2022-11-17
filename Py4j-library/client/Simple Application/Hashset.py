from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
s = gateway.jvm.java.util.HashSet()
s.add(1)
s.add('hello')
print(s)