# Protobuf

Protocol Buffers 是一种与语言、平台无关，可扩展的序列化结构化数据的方法，常用于通信协议，数据存储等等。相较于 JSON、XML，它更小、更快、更简单

## 安装

Mac

```bash
brew install protobuf
##检测是否安装成功

protoc --version
libprotoc 3.6.1
```

or 下载源代码编译

```sh
./autogen.sh
./configure
make check
make
make isntall
```

configure: WARNING: no configuration information is in third_party/googletest

需要下载 googletest，下载地址：<https://github.com/google/googletest/releases>，解压后放在`./protobuf-3.6.1/third_party/googletest`，然后执行`./autogen.sh`之后的

## 语法

```
syntax = "proto3";

service SearchService {
    rpc Search (SearchRequest) returns (SearchResponse);
}

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
}

message SearchResponse {
    ...
}
```

1、第一行（非空的非注释行）声明使用 `proto3` 语法。如果不声明，将默认使用 `proto2` 语法。同时我建议用 v2 还是 v3，都应当声明其使用的版本

2、定义 `SearchService` RPC 服务，其包含 RPC 方法 `Search`，入参为 `SearchRequest` 消息，出参为 `SearchResponse` 消息

3、定义 `SearchRequest`、`SearchResponse` 消息，前者定义了三个字段，每一个字段包含三个属性：类型、字段名称、字段编号

4、Protobuf 编译器会根据选择的语言不同，生成相应语言的 Service Interface Code 和 Stubs

[Protocol Buffers Language Guide (proto3)](https://developers.google.com/protocol-buffers/docs/proto3)

## 数据类型

| .proto Type | Notes                                                                                                                                           | C++ Type | Java Type  | Python Type[2] | Go Type | Ruby Type                      | C# Type    | PHP Type          | Dart Type |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------- | -------------- | ------- | ------------------------------ | ---------- | ----------------- | --------- |
| double      |                                                                                                                                                 | double   | double     | float          | float64 | Float                          | double     | float             | double    |
| float       |                                                                                                                                                 | float    | float      | float          | float32 | Float                          | float      | float             | double    |
| int32       | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32    | int        | int            | int32   | Fixnum or Bignum (as required) | int        | integer           | int       |
| int64       | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64    | long       | int/long[3]    | int64   | Bignum                         | long       | integer/string[5] | Int64     |
| uint32      | Uses variable-length encoding.                                                                                                                  | uint32   | int[1]     | int/long[3]    | uint32  | Fixnum or Bignum (as required) | uint       | integer           | int       |
| uint64      | Uses variable-length encoding.                                                                                                                  | uint64   | long[1]    | int/long[3]    | uint64  | Bignum                         | ulong      | integer/string[5] | Int64     |
| sint32      | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s.                            | int32    | int        | int            | int32   | Fixnum or Bignum (as required) | int        | integer           | int       |
| sint64      | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s.                            | int64    | long       | int/long[3]    | int64   | Bignum                         | long       | integer/string[5] | Int64     |
| fixed32     | Always four bytes. More efficient than uint32 if values are often greater than 228.                                                             | uint32   | int[1]     | int/long[3]    | uint32  | Fixnum or Bignum (as required) | uint       | integer           | int       |
| fixed64     | Always eight bytes. More efficient than uint64 if values are often greater than 256.                                                            | uint64   | long[1]    | int/long[3]    | uint64  | Bignum                         | ulong      | integer/string[5] | Int64     |
| sfixed32    | Always four bytes.                                                                                                                              | int32    | int        | int            | int32   | Fixnum or Bignum (as required) | int        | integer           | int       |
| sfixed64    | Always eight bytes.                                                                                                                             | int64    | long       | int/long[3]    | int64   | Bignum                         | long       | integer/string[5] | Int64     |
| bool        |                                                                                                                                                 | bool     | boolean    | bool           | bool    | TrueClass/FalseClass           | bool       | boolean           | bool      |
| string      | A string must always contain UTF-8 encoded or 7-bit ASCII text.                                                                                 | string   | String     | str/unicode[4] | string  | String (UTF-8)                 | string     | string            | String    |
| bytes       | May contain any arbitrary sequence of bytes.                                                                                                    | string   | ByteString | str            | []byte  | String (ASCII-8BIT)            | ByteString | string            |           |

## 相较 Protobuf，为什么不使用 XML？

- 更简单
- 数据描述文件只需原来的 1/10 至 1/3
- 解析速度是原来的 20 倍至 100 倍
- 减少了二义性
- 生成了更易使用的数据访问类
