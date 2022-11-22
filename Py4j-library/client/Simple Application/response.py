from py4j.java_gateway import JavaGateway
def Add_2_Num(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    gateway = JavaGateway()  # connect to the JVM    
    # addition_app = gateway.entry_point  # get the AdditionApplication instance
    value = gateway.entry_point.addition(num1,num2) # call the addition method
    return value
print(Add_2_Num(2,3))

