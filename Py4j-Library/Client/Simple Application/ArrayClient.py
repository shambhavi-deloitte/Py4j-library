from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
int_class = gateway.jvm.int
int_array = gateway.new_array(int_class,2)
int_array[0] = 1
int_array[1] = 2
for i in int_array:
    print(i)
    