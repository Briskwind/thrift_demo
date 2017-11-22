import sys
import os


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(path)

from python_tf.gen.demo import Demo

import thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():

    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Demo.Client(protocol)
    try:
        transport.open()
    except thrift.transport.TTransport.TTransportException:
        print('客户端连接错误')
        return

    client.ping()
    print('调用了ping()')

    sum_ = client.add(1, 2)
    print('add 结果 %d' % sum_)

    ret_dict = client.dict_return('key', 'value')
    print('服务器返回的字典', ret_dict.key, ret_dict.value)

    transport.close()


main()
