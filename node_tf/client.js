/**
 * Created by xufengxu on 2017/11/22.
 */
/**
 * Created by xufengxu on 2017/11/17.
 */
var thrift = require('thrift');
var Demo = require('./gen-nodejs/Demo');
var transport = thrift.TBufferedTransport;
var protocol = thrift.TBinaryProtocol;

var connection = thrift.createConnection("localhost", 9090, {
    transport: transport,
    protocol: protocol
});

connection.on('error', function (err) {
    assert(false, err);
});

var client = thrift.createClient(Demo, connection);


client.ping(function (err, response) {
    console.log('ping()');
});


client.add(1, 2, function (err, response) {
    console.log("add result:" + response);
});

client.dict_return('client_key', 'client_value', function (err, response) {
    console.log("dict_return:" + response.key, response.value);
    connection.end();
    // transport.end()

});


