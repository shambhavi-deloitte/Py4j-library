from py4j.java_gateway import JavaGateway
from py4j.java_collections import SetConverter, MapConverter, ListConverter
my_list = [3,2,1]
gateway = JavaGateway(auto_convert=True)
java_list = ListConverter().convert(my_list, gateway._gateway_client)
gateway.jvm.java.util.Collections.sort(java_list)
print("Before sort",my_list)
print("After sort",java_list)