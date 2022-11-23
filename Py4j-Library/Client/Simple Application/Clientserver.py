from py4j.java_gateway import JavaGateway
from py4j.clientserver import *
clientserver = ClientServer()
l = clientserver.jvm.java.util.ArrayList()
l.append(10)
l.append(1)
print(l)

