import thriftpy
from thriftpy.rpc import make_server

demo_thrift = thriftpy.load("demo.thrift", module_name="demo_thrift")

print('demo_thrift', dir(demo_thrift))


class ThriftpySevices(object):
    def ping(self):
        print("ping")
        return "pong"

    def add(self, a, b):
        return a + b

    def dict_return(self, key, name):
        print("dict_return", key, name)
        tem_dict = demo_thrift.my_dict()
        tem_dict.key = 'msg'
        tem_dict.value = '请求成功,来自 thriftpy server'
        return tem_dict


if __name__ == '__main__':
    server = make_server(demo_thrift.Demo, ThriftpySevices(), "127.0.0.1", 9090)
    print('Thriftpy Server 服务开启中...')
    try:
        server.serve()
    except KeyboardInterrupt:
        pass
