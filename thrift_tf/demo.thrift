
/**
 * The first thing to know about are types. The available types in Thrift are:
 *
 *  bool        Boolean, one byte
 *  i8 (byte)   Signed 8-bit integer
 *  i16         Signed 16-bit integer
 *  i32         Signed 32-bit integer
 *  i64         Signed 64-bit integer
 *  double      64-bit floating point value
 *  string      String
 *  binary      Blob (byte array)
 *  map<t1,t2>  Map from one type to another
 *  list<t1>    Ordered list of one type
 *  set<t1>     Set of unique elements of one type
 *
 * Did you also notice that Thrift supports C style comments?
 */




namespace cpp demo
namespace d demo
namespace dart demo
namespace java demo
namespace php demo
namespace perl demo
namespace haxe demo
namespace netcore demo



struct my_dict{
    1:string key
    2:string value
    
}


service Demo  {
   void ping(),
   my_dict dict_return(1:string key,2:string name),
   i32 add(1:i32 num1, 2:i32 num2),

}
