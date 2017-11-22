import json
import sys
import os


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(path)


from python_tf.gen.demo import Demo
from python_tf.gen.demo.ttypes import my_dict


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class DemoHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('服务器收到客户端的ping()调用')

    def add(self, n1, n2):
        print('收到客户端 add(%d,%d)' % (n1, n2))
        return n1 + n2

    def dict_return(self, key, name):
        print('来自 python server 收到 key, name:', key, name)
        tem_dict = my_dict()
        tem_dict.key = key
        tem_dict.value = '请求成功,来自 python server'

        return tem_dict


if __name__ == '__main__':
    handler = DemoHandler()
    processor = Demo.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print('服务已经开启')

    server.serve()
