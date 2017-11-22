import thriftpy
from thriftpy.rpc import make_client


pingpong_thrift = thriftpy.load("demo.thrift", module_name='demo_thrift')
client = make_client(pingpong_thrift.Demo, '127.0.0.1', 9090)


print("ping", client.ping())

print('add', client.add(2, 4))

print("dict_return", client.dict_return("1", "2"))
