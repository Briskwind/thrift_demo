/**
 * Created by xufengxu on 2017/11/22.
 */

var thrift = require("thrift");
var Demo = require("./gen-nodejs/Demo");
var RetDict = require("./gen-nodejs/demo_types").my_dict;


var server = thrift.createServer(Demo, {
    ping: function (result) {
        console.log("ping()");
        result(null);
    },

    add: function (n1, n2, result) {
        console.log("add(", n1, ",", n2, ")");
        result(null, n1 + n2);
    },

    dict_return: function (key, value, result) {
        console.log("dict_return:", key, ",", value);
        var tem_dict = new RetDict();
        tem_dict.key = 'server_key';
        tem_dict.value = '请求成功,来自 node server';
        result(null, tem_dict);
    }

});

server.listen(9090);
console.log('listening 9090');